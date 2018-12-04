from bs4 import BeautifulSoup
from day1_1 import simple_get

# need to forge the log-in safari cookies into this get request, getting bad
# content.

raw_html = simple_get('http://www.google.com')
html = BeautifulSoup(raw_html, 'html.parser')

for i, li in enumerate(html.select('pre')):
    print(i, li.text)
