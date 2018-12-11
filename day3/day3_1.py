# credit to u/TheHungryTurnip
# 'https://www.reddit.com/r/adventofcode/comments/a3d6wi/day_3_part_1_troubleshooting/'

import sys
sys.path.append('..')

from bs4 import BeautifulSoup  # nopep8
from scrape import simple_get  # nopep8
from adventcode_sessiondata import cookie  # nopep8
import re  # nopep8


raw_html = simple_get('https://adventofcode.com/2018/day/3/input', cookie)
html = BeautifulSoup(raw_html, 'html.parser')

stripped_html = html.text.split('\n')

# pop off the last element, which is an empty string
stripped_html.pop()


class Claim():

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f'({self.x}, {self.y}){self.w}x{self.h}'


claims = []

for item in stripped_html:
    d = re.split(' |,|: |x', item)
    c = Claim(int(d[2]), int(d[3]), int(d[4]), int(d[5]))
    claims.append(c)

grid = {}

for item in claims:
    for h in range(0, item.h):
        for w in range(0, item.w):
            coord = f'{item.x + w}x{item.y + h}'
            if coord in grid:
                grid[coord] += 1
            else:
                grid[coord] = 1

overlaps = 0

for item in grid:
    if grid[item] > 1:
        overlaps += 1

print(f'overlaps: {overlaps}')
