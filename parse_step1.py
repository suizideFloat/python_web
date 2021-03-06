import urllib
from bs4 import BeautifulSoup


URL = 'http://haunebu.raxys.net:5000/?p='


if __name__ == '__main__':
    for x in xrange(1, 11):
        url_str = '%s%d' % (URL, x)
        sock = urllib.urlopen(url_str)
        html_source = sock.read()
        sock.close()

        soup = BeautifulSoup(html_source)
        #print html_source
        table = soup.find('table', attrs={'class': 'table'})

        headings = (th.get_text() for th in table.find('tr').find_all('th'))

        datasets = []

        for row in table.findAll('tr')[1:]:
            datasets.append(zip(
                headings, (td.get_text() for td in row.find_all('td'))
            ))

        #print datasets

        for dataset in datasets:
            for field in dataset:
                print '{0:<16}: {1}'.format(field[0], field[1])

    #print soup('table')[0].prettify()

    #    for cell in row.findAll('td'):
    #        dataset = cell.findAll(text=True)
    #        print dataset
