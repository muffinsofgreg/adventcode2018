from bs4 import BeautifulSoup
from scrape import simple_get
from requests import post
from adventcode_sessiondata import cookie

# need to forge the log-in safari cookies into this get request, getting bad
# content.

# Needed cookie to get 200 response

raw_html = simple_get('https://adventofcode.com/2018/day/1/input', cookie)
html = BeautifulSoup(raw_html, 'html.parser')

stripped_html = html.text.split('\n')
new_html = []

try:
    for item in stripped_html:
        new_html.append(int(item))
except ValueError:
    print('valuerror')

print(sum(new_html))
