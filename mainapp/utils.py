from settings import ENCODING
import json
from sys import argv
from logging import getLogger
from logs.loggers import server_logger, client_logger
import traceback


def log(func):
    """
    Декоратор для логирования.
    Записывает в лог файл сообщение вида:
    Функция foo вызвана из функции main.
    Может быть использован только в
    client.py или server.py
    """

    def wrapper(*args, **kwargs):
        script_name = argv[0].split('/')[-1]
        call_from = traceback.extract_stack()[-2].name
        if script_name == 'client.py':
            logger = getLogger('client')
            logger.info(f'Функция {func.__name__} вызвана из функции {call_from}',
                        stacklevel=2)
        elif script_name == 'server.py':
            logger = getLogger('server')
            logger.info(f'Функция {func.__name__} вызвана из функции {call_from}',
                        stacklevel=2)
        else:
            raise Exception('Неизвестное имя скрипта')

        return func(*args, **kwargs)

    return wrapper


@log
def get_message(data):
    """
    Парсит сообщение из сокета и
    возвращает словарь
    """
    if isinstance(data, bytes):
        dict_string = data.decode(ENCODING)
        message = json.loads(dict_string)
        return message
    raise ValueError


@log
def send_message(socket, message):
    """
    Из словаря создает байты и передает
    """
    json_dict = json.dumps(message)
    encoded_message = json_dict.encode(ENCODING)
    socket.send(encoded_message)
