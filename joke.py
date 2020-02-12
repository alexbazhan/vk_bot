import urllib.request
import sys
from bs4 import BeautifulSoup
import requests


def getURL(url):
    
    try:
        load_url = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'})
        new_url  = urllib.request.urlopen(load_url)
        ANS = new_url.read()
    except urllib.error.HTTPError:
        ANS = 'Connect error'
    except urllib.error.URLError:
        ANS = 'URL error'

    return ANS

def get_tags(content):
    soup = BeautifulSoup(content, 'lxml')
    text = soup.find('div',{"class":'anekdot-content'}).text
    return text


def take_vk_msg():
    Page = getURL('https://anekdot-z.ru/random-anekdot')
    tags = get_tags(Page)
    return tags

def main(url):
    Page = getURL(url)
    tags = get_tags(Page)
    print(tags)


if __name__=='__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
        print('Done')
    else:
        print ('Укажите в качестве параметра нужный URL')
        main('https://anekdot-z.ru/random-anekdot')
