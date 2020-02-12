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
    name = ' '.join(soup.h1.text.split())
    info = soup.find('ul',{"class":'content-main-info'}).find_all('li')
    year = info[2].text
    genre = ' '.join(info[5].text.split())

    cont = soup.find('div', id='content-desc-text').text
    
    return "Название: {0} \n{1}\n{2}\n\n{3}".format(name,year,genre,cont)

def get_img(content):
    soup = BeautifulSoup(content, 'lxml')
    url_img = soup.find('div',{"class":'poster-block'})
    imga = requests.get('https://yummyanime.club' + url_img.img['src']).content
    with open('imga.jpg', "wb") as f:
            f.write(imga)

def save_file(file_name, text):  #сохранение
    
    new_file = open(file_name + '.txt','w',encoding = "utf- 8") # сохранение файла
    new_file.write(text)
    new_file.close()

def take_vk_msg():
    Page = getURL('https://yummyanime.club/random')
    tags = get_tags(Page)
    get_img(Page)
    return tags

def main(url):
    Page = getURL(url)
    tags = get_tags(Page)
    url_img = get_img(Page)
    #print(tags, url_img)
    save_file('anime', tags)


if __name__=='__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
        print('Done')
    else:
        print ('Укажите в качестве параметра нужный URL')
        main('https://yummyanime.club/random')
