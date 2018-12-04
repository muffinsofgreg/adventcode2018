from bs4 import BeautifulSoup
from day1_1 import simple_get
from requests import post

# need to forge the log-in safari cookies into this get request, getting bad
# content.

# Needed cookie to get 200 response
cookie = {'session': '53616c7465645f5fa781e68e30ca72571de02155c2b284a09d89968bbb63326bca1d811344eae5316641662f7f3e8230',
          '_gid': 'GA1.2.1346648579.1543826069',
          '_ga': 'GA1.2.1381619122.1543685303'}

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
