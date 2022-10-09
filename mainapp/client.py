from sys import argv
from socket import socket, AF_INET, SOCK_STREAM

from mainapp.settings import HOST, PORT, ACTION, MESSAGE, USER, ACTIONS
from utils import send_message, get_message


def make_dict_from_message(message, action):
    dict_message = {
        ACTION: action,
        MESSAGE: message,
        USER: 'testUser',
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
    sock.connect((host, port))
    dict_message = make_dict_from_message('Приветики!', ACTIONS.get('presence'))
    send_message(sock, dict_message)
    print(get_message(sock))
    sock.close()


if __name__ == '__main__':
    main()
