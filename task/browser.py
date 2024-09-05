import os
import sys
from collections import deque
import requests
from bs4 import BeautifulSoup


def try_exit(text):
    if text == 'exit':
        sys.exit()


def try_back(text, history):
    if text == 'back':
        if history:
            history.pop()
            if history:
                return history.pop()

        return None

    return text


def work_with_dir():
    dir_path = sys.argv[1]
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    os.chdir(dir_path)


def add_protocol(text):
    if not text.startswith('http://'):
        text = 'http://' + text

    return text


def is_correct(text):
    return '.' in text


def file_name(text):
    dot_index = text.index('.')
    return text[:dot_index]


def work_with_files(name, history):
    if os.path.exists(name):
        with open(name, 'r', encoding='utf-8') as old_f:
            for line in old_f:
                print(line, end='')
            print()
    elif is_correct(name):
        with open(file_name(name), 'w', encoding='utf-8') as new_f:
            history.append(file_name(name))
            r = requests.get(add_protocol(name))
            new_f.write(r.text)
            print(r.text)

    else:
        print('Invalid URL')


def main():
    work_with_dir()

    history = deque()

    while True:
        name = input()
        try_exit(name)

        name = try_back(name, history)
        if not name:
            continue

        work_with_files(name, history)


if __name__ == '__main__':
    main()
