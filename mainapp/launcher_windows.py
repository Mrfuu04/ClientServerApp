import subprocess
import argparse
from time import sleep

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    '-c',
    '--clients',
    type=int,
    help='Количество запускаемых клиентов',
    default=1,
)
args = arg_parser.parse_args()

PROCESSES = []

def main():
    PROCESSES.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
    for i in range(args.clients):
        sleep(0.5)
        PROCESSES.append(subprocess.Popen('python client.py', creationflags=subprocess.CREATE_NEW_CONSOLE))

if __name__ == '__main__':
    main()