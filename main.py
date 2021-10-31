#!/usr/bin/env python3
from lib.Loader import Loader
from lib.Statistics import Statistics
import argparse
from lib.Utils import get_headers, login

import gettext

tr = gettext.translation('argparse', 'translation', ['ru'], fallback=True)
argparse._ = tr.gettext
argparse.ngettext = tr.ngettext

cool_msg = """
     __  __ _      ___ _                _ _              
    |  \/  | |    / __| |_ __ _ _ _  __| (_)_ _  __ _ ___
    | |\/| | |__  \__ \  _/ _` | ' \/ _` | | ' \/ _` (_-<
    |_|  |_|____| |___/\__\__,_|_||_\__,_|_|_||_\__, /__/
                                                |___/    

    Статист по машинке (C) ediah

"""

def new_help(func):
    def printer():
        print(cool_msg)
        func()
    return printer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage = 'main.py [-h] [-l] [-u] (-s | -n N)')

    old_help = parser.print_help
    parser.print_help = new_help(old_help)

    mut = parser.add_mutually_exclusive_group()
    group = parser.add_argument_group('необходимая группа аргументов')
    parser.add_argument('-u', action='store_true', help='обновить принудительно')
    group.add_argument('-l', action='store_true', help='войти в систему из терминала')
    group.add_argument('-s', action='store_true', help='общая статистика')
    group.add_argument('-n', default='', help='поиск по фамилии с именем')
    args = parser.parse_args()

    if not (args.s or args.n or args.l):
        print(f'{__file__}: ошибка: аргументы -s, -n, -l: ожидался хотя бы один аргумент из группы')
        exit(1)

    if args.l:
        login()
        exit(0)

    headers = get_headers()

    ldr = Loader(headers, args.u)
    sts = Statistics(ldr.table)
    
    if args.s:
        sts.statTop(args.n)
    else:
        if args.n == '':
            print("Не указано имя для поиска!")
            exit(1)
        sts.statName(args.n)
