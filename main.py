from lib.Loader import Loader
from lib.Statistics import Statistics
import sys

if __name__ == '__main__':
    update = False
    name = 'КУТОН ФРАНСУА'
    
    for arg in sys.argv[1:]:
        if arg == '-u':
            update = True
        else:
            name = arg

    with open('headers.txt', 'r') as cookie:
        headers = eval(cookie.read())

    ldr = Loader(headers, update)
    sts = Statistics(ldr.table)
    sts.stat(name) 
