from bs4 import BeautifulSoup
from scrape import simple_get
from requests import post
from adventcode_sessiondata import cookie
import collections

raw_html = simple_get('https://adventofcode.com/2018/day/2/input', cookie)
html = BeautifulSoup(raw_html, 'html.parser')

stripped_html = html.text.split('\n')

# pop off the last element, which is an empty string
stripped_html.pop()

for i in range(len(stripped_html)):
    for j in range(len())

print(stripped_html)
