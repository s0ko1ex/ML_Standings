from lib.Loader import Loader
from lib.Statistics import Statistics
import sys

def helpMsg():
    print("Статист по машинке (C) ediah")
    print("Флаги:\n\t-h\tВывести это сообщение и выйти")
    print("\t-u\tОбновить принудительно\n\t-s\tОбщая статистика")
    print("\t-n\tПоиск по фамилии с именем")
    exit(0)

if __name__ == '__main__':
    update = False
    stats = False
    name = ''
    
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if arg == '-h':
            helpMsg()
        elif arg == '-u':
            update = True
        elif arg == '-s':
            stats = True
        elif arg == '-n':
            name = sys.argv[i+1]
    
    

    with open('headers.txt', 'r') as cookie:
        headers = eval(cookie.read())

    ldr = Loader(headers, update)
    sts = Statistics(ldr.table)
    
    if stats:
        sts.statTop(name)
    else:
        if name == '':
            print("Не указано имя для поиска!")
            exit(1)
        sts.statName(name)
