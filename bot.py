import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import urllib.request
import sys
from bs4 import BeautifulSoup
import anime_bot
import gismetio
import joke
from ochko import Ochko_session

def write_msg(user_id, message):
    vk.messages.send(user_id=user_id, random_id = random.getrandbits(64), message=message)

def write_msg_with_img(user_id, message, images):
    attachments = []
    for img in images:
        photo = upload.photo_messages(photos=img)[0]  
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
    vk.messages.send(user_id=user_id, random_id = random.getrandbits(64), attachment=','.join(attachments), message=message)
    
# API-ключ созданный ранее
token = ''

# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)
upload = vk_api.VkUpload(vk_session)

Ochko_players={}

# Работа с сообщениями
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            
            # Каменная логика ответа

            if event.user_id in Ochko_players:
                text = Ochko_players[event.user_id].take_message(request)
                if text == 'выход':
                    Ochko_players.pop(event.user_id)
                    write_msg(event.user_id, 'Вы вышли из игры')
                else:
                    cards_im = [('cards/' + card + '.jpg') for card in text[1]]
                    write_msg_with_img(event.user_id, text[0], cards_im)
            elif request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            elif request == 'аниме':
                anime = anime_bot.take_vk_msg()
                write_msg_with_img(event.user_id, anime, ['imga.jpg'])
            elif request == "погода":
                text = gismetio.take_vk_msg()
                write_msg(event.user_id, text)
            elif request == "анекдот":
                text = joke.take_vk_msg()
                write_msg(event.user_id, text)
            elif request == "21":
                Ochko_players[event.user_id] = Ochko_session()
                write_msg(event.user_id, "Напишите старт чтобы начать игру; чтобы выйти напишите выход")
            else:
                print(request,event.user_id)
                write_msg(event.user_id, "Возможные команды: привет, пока, 21, погода, анекдот")
                
