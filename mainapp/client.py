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
    with socket(AF_INET, SOCK_STREAM) as sock:
        host, port = get_host_and_port()
        try:
            sock.connect((host, port))
        except ConnectionRefusedError as e:
            logger.error(f'Подключение сброшено\n{e}')
            sys.exit(1)
        except OSError as e:
            print('Подключение уже установлено')
        print(f'Подключено к {host}:{port}')
        logger.info(f'Подключение к {(host, port)} успешно!')
        mode = input('Выбор режима (l)-слушать, (w)-писать:')
        while True:
            if mode == 'l':
                data = sock.recv(4096)
                print(data.decode('utf-8'))
            elif mode == 'w':
                message = input()
                sock.send(message.encode('utf-8'))
            else:
                mode = input('Выбор режима (l)-слушать, (w)-писать:')


if __name__ == '__main__':
    main()
