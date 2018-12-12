# credit to u/TheHungryTurnip for Part 1
# 'https://www.reddit.com/r/adventofcode/comments/a3d6wi/day_3_part_1_troubleshooting/'
# credit to u/evonfriedland for Part 2 - and for turning me on to NumPy
# 'https://www.reddit.com/r/adventofcode/comments/a2lesz/2018_day_3_solutions/

import sys
sys.path.append('..')

from bs4 import BeautifulSoup  # nopep8
from scrape import simple_get  # nopep8
from adventcode_sessiondata import cookie  # nopep8
import re  # nopep8
import numpy as np  # nopep8


raw_html = simple_get('https://adventofcode.com/2018/day/3/input', cookie)
html = BeautifulSoup(raw_html, 'html.parser')

stripped_html = html.text.split('\n')

# pop off the last element, which is an empty string
stripped_html.pop()


class Claim():

    def __init__(self, n, x, y, w, h):
        self.n = n
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f'{self.n}-({self.x}, {self.y}){self.w}x{self.h}'


claims = []

for item in stripped_html:
    d = re.split(' |,|: |x', item)
    c = Claim(d[0], int(d[2]), int(d[3]), int(d[4]), int(d[5]))
    claims.append(c)

fabric = np.zeros((1000, 1000))

for item in claims:
    n = item.n
    x = item.x
    y = item.y
    dx = item.w
    dy = item.h

    fabric[x:x + dx, y: y + dy] += 1

print(np.sum(fabric > 1))

for item in claims:
    n = item.n
    x = item.x
    y = item.y
    dx = item.w
    dy = item.h

    if np.all(fabric[x:x + dx, y:y + dy] == 1):
        print(n)
