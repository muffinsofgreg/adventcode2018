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

sample = ['#1360 @ 167,387: 19x14', '#1361 @ 578,871: 16x14']


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
    for w in range(item.w):
        for h in range(item.h):
            coord = f'{c.x + w}x{c.y + h}'
            if coord in grid:
                grid[coord] += 1
            else:
                grid[coord] = 1

print(grid)

overlaps = 0

for item in grid:
    if grid[item] > 0:
        overlaps += 1

print(f'overlaps: {overlaps}')
