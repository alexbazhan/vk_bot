import urllib.request
import sys
from bs4 import BeautifulSoup
import requests


def getURL(url):
    
    try:
        load_url = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'})
        new_url  = urllib.request.urlopen(load_url)
        ANS = new_url.read()#.decode(new_url.headers.get_content_charset())
    except urllib.error.HTTPError:
        ANS = 'Connect error'
    except urllib.error.URLError:
        ANS = 'URL error'

    return ANS

def get_tags(content):
    soup = BeautifulSoup(content, 'lxml')
    widget = soup.find('div',{"class":'widget__body'})
    days = widget.find_all('div',{"class":'w_date'})
    tempMX = widget.find_all('div',{"class":'maxt'})
    tempMN = widget.find_all('div',{"class":'mint'})
    text_days=[]
    text_all = ''
    for day in days:
        day = ' '.join(day.text.split())
        text_days.append(day)
    for i in range(len(tempMX)):
        maxt = tempMX[i].find('span',{"class":'unit unit_temperature_c'}).text
        text_all += '{0}: {1}\n'.format(text_days[i],maxt)
    return text_all


def take_vk_msg():
    Page = getURL('https://www.gismeteo.ru/weather-yaroslavl-4313/10-days/')
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
        main('https://www.gismeteo.ru/weather-yaroslavl-4313/10-days/')
