from bs4 import BeautifulSoup
from day1_1 import simple_get
# from htmlmin import minify

raw_html = simple_get('https://adventofcode.com/2018/day/1/input')
# minify_html = minify(raw_html)
html = BeautifulSoup(raw_html, 'html.parser')

for i, li in enumerate(html.select('pre')):
    print(i, li.text)
