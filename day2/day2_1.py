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

dupe_dict = {}

for item in stripped_html:
    dupe_dict[item] = collections.Counter(item).most_common(2)

threes = 0
twos = 0

for item in dupe_dict:
    if dupe_dict[item][0][1] == 2:
        twos += 1
        continue  # if the first duplicate is a 2, then don't count the rest

    if dupe_dict[item][0][1] == 3:
        threes += 1
    if dupe_dict[item][1][1] == 2:
        twos += 1

print(dupe_dict[item])
print(dupe_dict[item][0])
print(dupe_dict[item][0][1])
print()
print(threes)
print(twos)

# confirmed, returning the correct answer
print(threes * twos)
