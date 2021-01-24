from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from pylint import epylint as lint
import shutil
import datetime
import os
import logging


app = FastAPI()
root = 'D:\Desktop\python_content'                                  # корневая папка
py_files_folder = f'{root}\py_files'                                # папка с .py файлами
pylint_files_folder = f'{root}\pylint_files'                        # папка с отчетами pylint
today_folder = f'\{datetime.datetime.now().strftime("%Y-%m-%d")}'   # названеи директории текущего дня


if not os.path.isdir(f'{root}{today_folder}'):
    os.mkdir(f'{root}{today_folder}')

logging.basicConfig(filename=f'{root}{today_folder}\sample.log', level=logging.INFO)
log = logging.getLogger("ex")
log.info(f'Создана директория: {root}{today_folder}')

# создание необходимых директории
# if not os.path.isdir(py_files_folder):
#     logging.info(
#         f"User with IP={request.client.host}:{request.client.port} used {request.method} method to {request.url.path} with result: {result_text}")
#     os.mkdir(py_files_folder)
#
# if not os.path.isdir(pylint_files_folder):
#     os.mkdir(pylint_files_folder)
#
# if not os.path.isdir(f'{py_files_folder}{today_folder}'):
#     os.mkdir(f'{py_files_folder}{today_folder}')
#
# if not os.path.isdir(f'{pylint_files_folder}{today_folder}'):
#     os.mkdir(f'{pylint_files_folder}{today_folder}')


@app.post("/upload/python-files")
async def upload_py(file: UploadFile = File(...), message_format: str = None,
                    background_tasks: BackgroundTasks = BackgroundTasks()):
    message = ''
    msg_format = 'text'
    if message_format.lower() == 'json':
        msg_format = 'json'

    if file.filename[-3:] != '.py':
        message = 'Получен файл с неправилным расширением. Необходим файл с расширением .py'
        log.warning(f'Получен файл с неправилным расширением: {file.filename}\n'
                    f'Необходим файл с расширением .py')
    else:
        file_name = file.filename
        file_path = f'{root}{today_folder}' \
                    f'\{file.filename[:-3]}_' \
                    f'{datetime.datetime.now().strftime("%H-%M-%S")}' \
                    f'{file.filename[-3:]}'
        try:
            with open(file_path, 'wb') as buffer:
                shutil.copyfileobj(file.file, buffer)

        except FileNotFoundError:
            message = 'Не удалось сохранить загруженный файл на диске'
            log.exception(f'Не удалось сохранить загруженный файл на диске: {FileNotFoundError}')
        except Exception:
            message = 'Ошибка сервера'
            log.exception(f'Ошибка сервера: {Exception}')
        else:
            message = 'Файл успешно загружен и начaлся статический анализ с использованием pylint'
            log.info(f'Файл "{file_name}" успешно загружен и начaлся статический анализ с использованием pylint')
            background_tasks.add_task(pylint_analyse, file_path, file_name, msg_format)
    return {f'message': message}


def pylint_analyse(file_path: str, file_name: str, msg_format: str = None):
    py_file_path = f'{py_files_folder}{today_folder}\{file_name}'
    if msg_format == 'json':
        log.info(f'Начало статического анализа файла "{file_name}" с вывоводом результата в формате JSON')
        (pylint_stdout, pylint_stderr) = lint.py_run(command_options=f'{file_path} --output-format={msg_format}',
                                                     return_std=True)
        file_ext = '.json'
    else:
        log.info(f'Начало статического анализа файла "{file_name}" с вывоводом результата в формате TEXT')
        (pylint_stdout, pylint_stderr) = lint.py_run(command_options=f'{file_path}', return_std=True)
        file_ext = '.txt'

    pylint_file_path = f'{root}{today_folder}' \
                       f'\{file_name[:-3]}_{datetime.datetime.now().strftime("%H-%M-%S")}' \
                       f'{file_ext}'
    try:
        log.info(f'Запись отчета статического анализа файла "{file_name}" в файл "{pylint_file_path}"')
        with open(pylint_file_path, 'w') as file:
            file.write(f'{pylint_stderr.getvalue()}\n{pylint_stdout.getvalue()}')
    except FileNotFoundError:
        log.exception(f'Не удалось сохранить отчет статического анализа файла "{file_name}" в файл "{pylint_file_path}": {FileNotFoundError}')
    except Exception:
        log.exception(f'Ошибка сервера: {Exception}')
    else:
        log.info(f'Отчет статического анализа файла "{file_name}" успешно записан в файл "{pylint_file_path}"')


if __name__ == '__main__':
    (pylint_stdout, pylint_stderr) = lint.py_run(command_options='py_files\\2021-01-23\\main_12-00-03.py --output-format=json',
                                                 return_std=True)

    print(pylint_stdout.getvalue())
    print('-----------------')
    print(pylint_stderr.getvalue())
