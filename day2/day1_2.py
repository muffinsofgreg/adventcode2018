from bs4 import BeautifulSoup
from scrape import simple_get
from requests import post
from adventcode_sessiondata import cookie

raw_html = simple_get('https://adventofcode.com/2018/day/1/input', cookie)
html = BeautifulSoup(raw_html, 'html.parser')

stripped_html = html.text.split('\n')
new_html = []

# This actually achieves what I wanted buy by error. It strips the asci + from the strings,
# but leaves the "-" when converting to int.

try:
    for item in stripped_html:
        new_html.append(int(item))
except ValueError:
    print('valuerror')

dict_count = {}
counter = 0


def count(num):
    global counter
    i = 0

    while i < num:

        for item in new_html:
            counter += item
            if counter in dict_count:
                print("Here!!!!", counter)
                break
            else:
                dict_count[counter] = 1

        if counter in dict_count:
            break
        i += 1


count(500)
print(counter)
