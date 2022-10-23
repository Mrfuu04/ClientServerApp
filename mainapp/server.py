from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
from logging import getLogger
import logs.loggers.server_logger
from utils import send_message, get_message
from settings import HOST, PORT, ACTIONS, USER, ACTION

logger = getLogger('server')


def get_server_response(message):
    if message.get(ACTION) == ACTIONS.get('presence') and \
            message.get(USER) == 'testUser':
        response = {
            'response': 200,
            'text': 'ok'
        }
    else:
        response = {
            'response': 404,
            'text': 'bad request'
        }
    return response


def get_host_and_port():
    if '-p' and '-h' in argv:
        host, port = argv[3], int(argv[-1])
    else:
        host, port = HOST, PORT
    return host, port


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    host, port = get_host_and_port()
    sock.bind((host, port))
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        logger.info(f'Установлено соединение с {addr}')
        message = get_message(client)
        logger.info(f'Получение сообщение от {addr}\n{message}')
        server_response = get_server_response(message)
        send_message(client, server_response)
        logger.info(f'{server_response} отправлено {addr}')
        client.close()
        logger.info(f'Соединение с {addr} закрыто')


if __name__ == '__main__':
    main()
