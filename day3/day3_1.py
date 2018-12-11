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


# sample = ['#1 @ 483,830: 24x18', '#2 @ 370,498: 21x17', '#3 @ 403,823: 25x21', '#4 @ 619,976: 20x15', '#5 @ 123,385: 15x26', '#6 @ 484,592: 11x19', '#7 @ 394,960: 28x14', '#8 @ 730,592: 26x20', '#9 @ 975,963: 16x26', '#10 @ 452,496: 18x18']

# sample2 = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']


class Claim():

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f'({self.x}, {self.y}){self.w}x{self.h}'


claims = []

# test = sample[0]
# d = re.split(' |,|: |x', test)
# c = Claim(int(d[2]), int(d[3]), int(d[4]), int(d[5]))
# claims.append(c)
# print(test)
# print(d)
# print(c)
# print(claims)


for item in stripped_html:
    # print(item, "\n")
    d = re.split(' |,|: |x', item)
    # print(d, "\n")
    c = Claim(int(d[2]), int(d[3]), int(d[4]), int(d[5]))
    # print(c, "\n")
    claims.append(c)
    # print(claims, "\n")

grid = {}

for item in claims:
    # print("item: ", item)
    for h in range(0, item.h):
        # print("h: ", h)
        for w in range(0, item.w):
            # print("w: ", w)
            # print("item.x: ", item.x, ", item.y: ", item.y)
            coord = f'{item.x + w}x{item.y + h}'
            # print("coord: ", coord)
            if coord in grid:
                grid[coord] += 1
            else:
                grid[coord] = 1

overlaps = 0

for item in grid:
    if grid[item] > 1:
        overlaps += 1

print(f'overlaps: {overlaps}')
