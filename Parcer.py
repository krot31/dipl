import requests
from bs4 import BeautifulSoup
from lxml import html

import csv
from datetime import datetime
from multiprocessing import Pool

def get_html(url):
    r = requests.get(url)
    #print(r.text)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', class_="table table-condensed table-hover table-clickable showcase-table table-sortable").find_all('td', class_="text-right")
    tds1 = soup.find('table', class_="table table-condensed table-hover table-clickable showcase-table table-sortable").find_all('tr', class_=None)
    leage = soup.find('td', class_=None)
    links = []
    k=0

    for td in tds:
        a = td.find('div', class_=None)
        links.append(a)
        k+=1
    print("k=",k)
    return links

    # for td in tds1:
    #     #a = td.find('td', class_=None)
    #     a = td.find('td', class_=None)
    #     k+=1
    #     print(k)
    # return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        name = soup.find().text.strip()
    except:
        name = ''
    try:
        cost = soup.find().text.strip()
    except:
        cost = ''

    data = {'name': name,
            'cost':cost}
    return data

def write_csv(data):
    with open('docCost.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['cost']))
        print(data['name'], 'parsed')


def main():
    start = datetime.now()

    url = 'https://funpay.ru/chips/16/'
    all_links = get_all_links(get_html(url))

    print(all_links)

    # html=get_html(url)
    # data = get_page_data(html)
    # write_csv(data)
    # end = datetime.now()
    # total = end - start
    # print(str(total))



if __name__ == '__main__':
    main()