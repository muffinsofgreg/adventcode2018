# credit to u/TheHungryTurnip
# 'https://www.reddit.com/r/adventofcode/comments/a3d6wi/day_3_part_1_troubleshooting/'

import sys
sys.path.append('..')

from bs4 import BeautifulSoup  # nopep8
from scrape import simple_get  # nopep8
from adventcode_sessiondata import cookie  # nopep8
import re  # nopep8


raw_html = simple_get('https://adventofcode.com/2018/day/4/input', cookie)
html = BeautifulSoup(raw_html, 'html.parser')

stripped_html = html.text.split('\n')

# pop off the last element, which is an empty string
stripped_html.pop()


