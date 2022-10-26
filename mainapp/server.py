from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
from select import select
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
    with socket(AF_INET, SOCK_STREAM) as sock:
        host, port = get_host_and_port()
        sock.bind((host, port))
        sock.listen(5)
        sock.settimeout(1)

        client_sockets = []
        messages = []
        while True:
            try:
                client, addr = sock.accept()
            except TimeoutError as e:
                pass
            else:
                client_sockets.append(client)
                logger.info(f'Установлено соединение с {addr}')
                print(f'Установлено соединение с {addr}')
            finally:
                writers_list, getters_list = [], []
                try:
                    writers_list, getters_list, _ = select(client_sockets, client_sockets, [], 0)
                except OSError:
                    pass
                if writers_list:
                    for writer in writers_list:
                        try:
                            data = writer.recv(4096)
                            message = data.decode('utf-8')
                            messages.append(message)
                            logger.info(f'Получение сообщение от {addr}\n{message}')
                        except Exception:
                            client_sockets.remove(client)
                            logger.info(f'Соединение с {addr} закрыто')
                if getters_list and messages:
                    message = messages[0]
                    del messages[0]
                    for getter in getters_list:
                        try:
                            getter.send(message.encode('utf-8'))
                        except Exception:
                            client_sockets.remove(getter)
                            logger.info(f'Соединение с {addr} закрыто')


if __name__ == '__main__':
    main()
