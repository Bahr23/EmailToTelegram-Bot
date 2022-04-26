from urllib import response
from config import *
import json


def get_data():
    with open('chats.json', 'r') as f:
        return json.loads(f.read())

def save_data(data):
    with open('chats.json', 'w') as f:
        f.write(json.dumps(data, indent=4))


def add_chat(subject, chat_id):
    if chat_id > 0:
        return False
    if not subject:
        return False
    response = True
    data = get_data()
    if data:
        for c in data:
            if c['id'] == chat_id:
                response = False
                break
    if response:
        data.append({
            'subject': subject,
            'id': chat_id
        })
        save_data(data)
    return response


def remove_chat(chat_id):
    response = False
    try:
        chat_id = int(chat_id)
        data = get_data()
        if data:
            for c in data:
                if c['id'] == chat_id:
                    response = True
                    data.remove(c)
                    save_data(data)
                    break
    except:
        response = False
    return response

def get_chats():
    data = get_data()
    if data:
        text = ''
        for c in data:
            text += f"<code>{c['id']}</code> - {c['subject']}\n"
    else:
        text = 'Отсутствуют'
    return text