import re
from urllib import response
from bs4 import BeautifulSoup
import json


def get_message_profile(html):
    soup = BeautifulSoup(html, 'lxml')

    body = []

    for event in soup.find_all('td', class_='event-detail'):
        res = {
            'title': event.find('a').text,
            'href': event.find('a')['href']
        }
        body.append(res)

    for interface in soup.find_all('div', class_='interface'):
        res = {
            'title': interface.find('h3', class_='title').text.replace('<', '≪').replace('>', '≫') ,
            'body': []
        }

        pre = interface.find('pre')
        if pre:
            res['body'] = pre.text.replace('<', '≪').replace('>', '≫') 
        else:
            for th in interface.find_all('th'):
                res['body'].append({
                    'name': th.text.replace('<', '≪').replace('>', '≫') ,
                    'content': th.find_next('td').text.replace('<', '≪').replace('>', '≫') 
                })
        body.append(res)
    return body
