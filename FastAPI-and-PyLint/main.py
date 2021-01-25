import argparse

import uvicorn
from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from pylint import epylint as lint
import shutil
import datetime
import os
import logging


app = FastAPI()
root = os.path.join(os.getcwd(), 'python_content')                                     # корневая папка
today_folder = os.path.join(root, f'{datetime.datetime.now().strftime("%Y-%m-%d")}')   # названеи директории текущего дня

if not os.path.exists(root):
    os.mkdir(root)

if not os.path.exists(today_folder):
    os.mkdir(today_folder)

logging.basicConfig(filename=os.path.join(today_folder, 'sample.log'), level=logging.INFO)
log = logging.getLogger("ex")
log.info(f'Создана директория: {today_folder}')


@app.get("/python-files/pylint-report")
async def get_report(file_name: str):

    message = ''
    filename = file_name.split('.')
    file_path = os.path.join(today_folder, f'{file_name}')
    log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
             f'Запрос на полученеи отчета статического анализа "{filename[0]}.py"')
    try:
        if not os.path.exists(file_path):
            message = f'Не удалось найти файл "{filename}"'
        else:
            with open(file_path, 'r') as buffer:
                message = buffer.read()
            log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                         f'Отправка отчета статического анализа файла "{filename[0]}.py" клиенту')
    except Exception:
        message = f'Ошибка сервера'
        log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: {message}: {Exception}')
    return {f'message': message}


@app.post("/python-files/upload")
async def upload_py(file: UploadFile = File(...), message_format: str = None,
                    background_tasks: BackgroundTasks = BackgroundTasks()):

    message = ''
    msg_format = 'text'
    if message_format.lower() == 'json':
        msg_format = 'json'

    log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
             f'Запрос на выполнение статического анализа файла "{file.filename}" '
             f'с выводом отчета в формате {msg_format}')

    if file.filename[-3:] != '.py':
        message = f'Получен файл "{file.filename}" с неправилным расширением. Необходим файл с расширением .py'
        log.warning(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: {message}')
    else:
        if not os.path.exists(today_folder):
            os.mkdir(today_folder)

        file_name = f'{file.filename[:-3]}_{datetime.datetime.now().strftime("%H-%M-%S")}'
        file_path = os.path.join(today_folder, f'{file_name}.py')
        try:
            with open(file_path, 'wb') as buffer:
                shutil.copyfileobj(file.file, buffer)
        except Exception:
            message = f'Ошибка сервера'
            log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: {message}: {Exception}')
        else:
            message = f'Файл "{file.filename}" успешно загружен, ' \
                      f'сохранен под названием "{file_name}.py" ' \
                      f'и начaлся статический анализ с использованием pylint'
            log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: {message}')
            background_tasks.add_task(pylint_analyse, file_path, file_name, msg_format)
    return {f'message': message}


def pylint_analyse(file_path: str, file_name: str, msg_format: str = None):
    if msg_format == 'json':
        log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                 f'Начало статического анализа файла "{file_name}.py" с вывоводом результата в формате JSON')
        (pylint_stdout, pylint_stderr) = lint.py_run(command_options=f'{file_path} --output-format={msg_format}',
                                                     return_std=True)
        file_ext = '.json'
    else:
        log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                 f'Начало статического анализа файла "{file_name}.py" с вывоводом результата в формате TEXT')
        (pylint_stdout, pylint_stderr) = lint.py_run(command_options=f'{file_path}', return_std=True)
        file_ext = '.txt'

    pylint_file_path = os.path.join(today_folder, f'{file_name}{file_ext}')
    try:
        log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                 f'Запись отчета статического анализа файла "{file_name}.py" в файл "{pylint_file_path}"')
        with open(pylint_file_path, 'w') as file:
            file.write(f'{pylint_stderr.getvalue()}\n{pylint_stdout.getvalue()}')
    except Exception:
        log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                      f'Ошибка сервера: {Exception}')
    else:
        log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                 f'Отчет статического анализа файла "{file_name}.py" успешно записан в файл "{pylint_file_path}"')


if __name__ == '__main__':
    # Здесь идет блок кода для работы с аргументами командной строки
    parser = argparse.ArgumentParser(description='FastAPI and PyLint.')
    # Аргумент для хоста
    parser.add_argument('-host', type=str, default="127.0.0.1", help='host ip-address')
    # Аргумент для порта
    parser.add_argument('-port', type=int, default=5000, help='host port')
    # Аргумент для debug режима
    parser.add_argument('-debug', type=bool, default=False, help='Launch in debug mode?')

    args = parser.parse_args()
    print(f"Host = {args.host}; port = {args.port}")
    print(f"Debug mode: {args.debug}")

    # Запуск сервера с заданными параметрами
    uvicorn.run("main:app", host=args.host, port=args.port, reload=args.debug, access_log=args.debug)
