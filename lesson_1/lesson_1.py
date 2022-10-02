# ----- task 1 ----- #
# Каждое из слов «разработка», «сокет», «декоратор» представить в
# строковом формате и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в
# формат Unicode и также проверить тип и содержимое переменных.


def type_and_content_checker(words_array):
    for data in words_array:
        print(f'Тип - {type(data)}\nСодержимое - {data}')
    print(f'{"-" * 50}')


test_words = ('разработка', 'сокет', 'декоратор')
unicoded_words = ('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                  '\u0441\u043e\u043a\u0435\u0442',
                  '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')

type_and_content_checker(test_words)
type_and_content_checker(unicoded_words)


# ----- task 2 ----- #
# Каждое из слов «class», «function», «method» записать в байтовом типе.
# Сделать это необходимо в автоматическом, а не ручном режиме, с помощью
# добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя
# методы encode, decode или функцию bytes) и определить тип, содержимое и
# длину соответствующих переменных.


def automaticaly_to_byte_type(words_array):
    for word in words_array:
        byted = eval(f'b"{word}"')
        print(type(byted))


test_words = ('class', 'function', 'method')
automaticaly_to_byte_type(test_words)


# ----- task 3 ----- #
# Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе. Важно: решение должно быть
# универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.


def check_can_be_bytes(words_array):
    for word in words_array:
        try:
            eval(f'b"{word}"')
        except SyntaxError:
            print(f'Слово "{word}" невозможно записать в байтовом виде')


test_words = ('attribute', 'класс', 'функция', 'type')

check_can_be_bytes(test_words)


# ----- task 4 ----- #
# Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное
# преобразование (используя методы encode и decode).


def encode_and_decode(words_array):
    for word in words_array:
        encoded = word.encode('utf-8')
        print(f'Байтовое представление - {encoded}')
        decoded = encoded.decode('utf-8')
        print(f'Обратное преобразование - {decoded}')
        print('-' * 50)


test_words = ('разработка', 'администрирование', 'protocol', 'standard')

encode_and_decode(test_words)


# ----- task 5 ----- #
# Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовывает результат из байтовового типа данных в
# строковый без ошибок для любой кодировки операционной системы.


def ping_resources(resource_array):
    """
    В функции применяю detect из chardet т.к
    на Windows в stdout выдает несколько кодировок
    """
    import subprocess
    import platform
    from chardet import detect
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    for resource in resource_array:
        args = ('ping', param, '2', resource)
        with subprocess.Popen(args, stdout=subprocess.PIPE) as process:
            for out in process.stdout:
                detected_encoding = detect(out)
                utf = out.decode(detected_encoding['encoding']).encode('utf-8')
                print(utf.decode('utf-8'))
            print('-' * 50)


resources = ('yandex.ru', 'youtube.com')

ping_resources(resources)


# ----- task 6 ----- #
# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Далее забыть о том, что
# мы сами только что создали этот файл и исходить из того, что перед нами файл в
# неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК
# вне зависимости от того, в какой кодировке он был создан.


def open_and_read_txt(file):
    with open(file, encoding='utf-8') as f:
        for line in f.readlines():
            print(line)


open_and_read_txt('test_file.txt')
