from bs4 import BeautifulSoup
from scrape import simple_get
from requests import post
from adventcode_sessiondata import cookie
import collections

raw_html = simple_get('https://adventofcode.com/2018/day/2/input', cookie)
html = BeautifulSoup(raw_html, 'html.parser')

global stripped_html
stripped_html = html.text.split('\n')

# pop off the last element, which is an empty string
stripped_html.pop()

# stripped_html = ['abcd', 'abdc', 'bbdc', 'ahct', 'thys', 'usyd']


def find_them():
    for i in range(len(stripped_html)):
        for j in range(i + 1, len(stripped_html)):
            count = 0

            for k in range(len(stripped_html[1])):
                if stripped_html[i][k] != stripped_html[j][k]:
                    count += 1
                    if count > 1:
                        break
                else:
                    pass
                if k == 25 and count <= 1:
                    print(stripped_html[i], stripped_html[j])
                    return (stripped_html[i], stripped_html[j])
                else:
                    pass


answer = ""
for a, b in find_them():
    if a == b:
        answer += a
    else:
        pass
print(answer)
