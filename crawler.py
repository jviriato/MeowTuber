from bs4 import BeautifulSoup as bs
cat_names = []
soup = bs(open("gatos.html"), "html.parser")
for tr in soup.find_all('tr'):
    tds = tr.find_all('td')[0].text
    if "Nomes" not in tds:
        cat_names.append(tds)

file = open('cat_names.txt', 'w+')
for cat_name in cat_names:
    file.write(cat_name + '\n')

file.close()