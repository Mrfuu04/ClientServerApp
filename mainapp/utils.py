from mainapp.settings import ENCODING
import json


def get_message(socket):
    """
    Парсит сообщение из сокета и
    возвращает словарь
    """
    data = socket.recv(1000000)
    if isinstance(data, bytes):
        dict_string = data.decode(ENCODING)
        message = json.loads(dict_string)
        return message
    raise ValueError


def send_message(socket, message):
    """
    Из словаря создает байты и передает
    """
    json_dict = json.dumps(message)
    encoded_message = json_dict.encode(ENCODING)
    socket.send(encoded_message)

