import urllib
from bs4 import BeautifulSoup

url = "http://haunebu.raxys.net:5000/?p="
for x in range(1, 11):
    url_str = url + str(x)
    sock = urllib.urlopen(url_str)
    x += 1
    htmlSource = sock.read()
    sock.close()
    soup = BeautifulSoup(htmlSource)
#print htmlSource
    table = soup.find('table', attrs={'class': 'table'})

    headings = [th.get_text() for th in table.find("tr").find_all("th")]

    datasets = []



    for row in table.findAll("tr")[1:]:
        dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
        datasets.append(dataset)

#print datasets

    for dataset in datasets:
        for field in dataset:
            print "{0:<16}: {1}".format(field[0], field[1])

#print soup('table')[0].prettify()

#    for cell in row.findAll("td"):
#        dataset = cell.findAll(text=True)
#        print dataset
