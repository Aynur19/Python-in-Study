from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from pylint import epylint as lint
import shutil
import datetime
import os
import logging


app = FastAPI()
root = 'D:\Desktop\python_content'                                  # корневая папка
# py_files_folder = f'{root}\py_files'                                # папка с .py файлами
# pylint_files_folder = f'{root}\pylint_files'                        # папка с отчетами pylint
today_folder = f'\{datetime.datetime.now().strftime("%Y-%m-%d")}'   # названеи директории текущего дня


if not os.path.isdir(f'{root}{today_folder}'):
    os.mkdir(f'{root}{today_folder}')

logging.basicConfig(filename=f'{root}{today_folder}\sample.log', level=logging.INFO)
log = logging.getLogger("ex")
log.info(f'Создана директория: {root}{today_folder}')


@app.get("/python-files/pylint-report")
async def upload_py(file_name: str):

    message = ''
    filename = file_name.split('.')
    file_path = f'{root}{today_folder}\{filename[0]}.{filename[1]}'
    log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
             f'Запрос на полученеи отчета статического анализа "{filename[0]}.py"')
    try:
        with open(file_path, 'r') as buffer:
            message = buffer.read()
    except FileNotFoundError:
        message = f'Не удалось найти файл "file_name"'
        log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: {message}: {FileNotFoundError}')
    except Exception:
        message = f'Ошибка сервера'
        log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: {message}: {Exception}')
    else:
        log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                 f'Отправка отчета статического анализа файла "{filename[0]}.py" клиенту')
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
        file_name = f'{file.filename[:-3]}_{datetime.datetime.now().strftime("%H-%M-%S")}'
        file_path = f'{root}{today_folder}\{file_name}.py'
        try:
            with open(file_path, 'wb') as buffer:
                shutil.copyfileobj(file.file, buffer)

        except FileNotFoundError:
            message = f'Не удалось сохранить загруженный файл на диске'
            log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: {message}: {FileNotFoundError}')
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

    pylint_file_path = f'{root}{today_folder}\{file_name}{file_ext}'
    try:
        log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                 f'Запись отчета статического анализа файла "{file_name}.py" в файл "{pylint_file_path}"')
        with open(pylint_file_path, 'w') as file:
            file.write(f'{pylint_stderr.getvalue()}\n{pylint_stdout.getvalue()}')
    except FileNotFoundError:
        log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                      f'Не удалось сохранить отчет статического анализа файла "{file_name}.py" '
                      f'в файл "{pylint_file_path}": {FileNotFoundError}')
    except Exception:
        log.exception(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                      f'Ошибка сервера: {Exception}')
    else:
        log.info(f'{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M.%S")}: '
                 f'Отчет статического анализа файла "{file_name}.py" успешно записан в файл "{pylint_file_path}"')


if __name__ == '__main__':
    (pylint_stdout, pylint_stderr) = lint.py_run(command_options='py_files\\2021-01-23\\main_12-00-03.py --output-format=json',
                                                 return_std=True)

    print(pylint_stdout.getvalue())
    print('-----------------')
    print(pylint_stderr.getvalue())
