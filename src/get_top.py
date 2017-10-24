from sys import argv
from utils import get_top_n

"""
Currently, this is a command line utility that prints my
top n songs, tab indented, for any three "terms" (long-term, medium-term, 
or short-term) to stdout. If no term is specified, it defaults to short-term.
USAGE:
$ python3.x get_top.py long_term 1
range: long_term
    LITE SPOTS, KAYTRANADA
$ python3.x get_top.py 2
range: short_term
    Crew, GoldLink
    Navajo, Masego
"""

def main(user='ariopp', n=5, term='short_term'):
    ans = get_top_n(user, n, term)
    for i in sorted(ans):
        song = ans[i][0] 
        artist = ans[i][1]
        print(song + ",", artist)

if __name__ == "__main__":
    n = int(argv[-1])
    if len(argv) == 3:
        des_term = argv[-2]
        main('ariopp', n, term=des_term)
    else:
        main(user='ariopp', n=n)