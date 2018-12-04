from bs4 import BeautifulSoup
from scrape import simple_get
from requests import post

# Needed cookie to get 200 response
cookie = {'session': '53616c7465645f5fa781e68e30ca72571de02155c2b284a09d89968bbb63326bca1d811344eae5316641662f7f3e8230',
          '_gid': 'GA1.2.1346648579.1543826069',
          '_ga': 'GA1.2.1381619122.1543685303'}

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
        i += 1


count(15)
print(counter)
print(dict_count)
