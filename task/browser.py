import os
import sys
from collections import deque

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


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


def is_correct(text):
    return '.' in text


def contains(text, cur_list):
    return text in cur_list


def file_name(text):
    dot_index = text.index('.')
    return text[:dot_index]


def work_with_dir():
    dir_path = sys.argv[1]
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    os.chdir(dir_path)


def work_with_files(name, stack):
    websites = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}

    if os.path.exists(name):
        with open(name, 'r', encoding='utf-8') as old_f:
            for line in old_f:
                print(line, end='')
            print()
    elif is_correct(name) and contains(name, websites.keys()):
        with open(file_name(name), 'w', encoding='utf-8') as new_f:
            print(websites[name])
            new_f.write(websites[name])
            stack.append(name)
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
