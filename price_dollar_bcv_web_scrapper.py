import requests, certifi
from bs4 import BeautifulSoup


def scrape():
    url = 'https://www.bcv.org.ve/'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_dollar = soup.select_one('div.col-sm-6.col-xs-6.centrado').text
    print(price_dollar)


if __name__ == '__main__':
    scrape()

