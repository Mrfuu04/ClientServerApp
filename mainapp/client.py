import sys
from sys import argv
from logging import getLogger
from socket import socket, AF_INET, SOCK_STREAM

import logs.loggers.client_logger
from settings import HOST, PORT, ACTION, MESSAGE, USER, ACTIONS
from utils import send_message, get_message

logger = getLogger('client')


def make_dict_from_message(message, username, action):
    dict_message = {
        ACTION: action,
        MESSAGE: message,
        USER: username,
    }
    return dict_message


def get_host_and_port():
    try:
        host = argv[1]
        port = argv[2]
    except:
        host = HOST
        port = PORT
    return host, port


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    host, port = get_host_and_port()
    try:
        sock.connect((host, port))
    except ConnectionRefusedError as e:
        logger.error(f'Подключение сброшено\n{e}')
        sys.exit(1)
    else:
        logger.info(f'Подключение к {(host, port)} успешно!')
    dict_message = make_dict_from_message('Приветики!', 'testUser', ACTIONS.get('presence'))
    send_message(sock, dict_message)
    logger.info(f'Сообщение {dict_message} отправлено\n{sock}')
    logger.info(f'Получено сообщение от сервера {get_message(sock)}')
    sock.close()


if __name__ == '__main__':
    main()
