from bs4 import BeautifulSoup as bs
cat_names = []
soup = bs(open("gatos.html"), "html.parser")
for tr in soup.find_all('tr'):
    for l in range(0,len(tr.find_all('td'))):
        tds = tr.find_all('td')[l].text
        if "Nomes" not in tds and tds != "":
            cat_names.append(tds)

file = open('cat_names.txt', 'w+')
for cat_name in cat_names:
    file.write(cat_name + '\n')

file.close()