from bs4 import BeautifulSoup

with open('sample1.html') as f:
    raw_html = f.read()
    html = BeautifulSoup(raw_html, 'html.parser')
    for p in html.select('p'):
        print(p.attrs.get('id'))
        break