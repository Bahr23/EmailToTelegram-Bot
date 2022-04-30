import time
import logging

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from chatsMananger import *
from htmlParser import *

from imap_tools import MailBox


def get_message_text(body):
    text = ''
    for i in body:
        if 'href' in i.keys():
            text += f"\n<b><a href='{i['href']}'>{i['title']}</a></b>"
        else:
            text += f"\n\n<b>{i['title']}</b>"
            if type(i['body']) == str:
                text += f"\n<code>{i['body']}</code>"
            else:
                for b in i['body']:
                    if 'http' in b['content'][0:4]:
                        text += f"\n<i>{b['name']}</i> {b['content']}"
                    else:
                        text += f"\n<i>{b['name']}</i> <code>{b['content']}</code>"

    return text


def last_email(bot):
    while True:
        chats = get_data()
        with MailBox(IMAP4_SERVER).login(EMAIL_LOGIN, EMAIL_PASSWOARD, initial_folder='Errors') as mailbox:
            messages = mailbox.fetch()
            for msg in messages:
                for chat in chats:
                    if chat['subject'] in msg.subject:
                        with open('email_list.txt', 'r') as f:
                            email_list = f.read().split(',')
                        if msg.obj['Message-id'] not in email_list:
                        
                            body = msg.html
                            message_profile = get_message_profile(body)

                            text = get_message_text(message_profile)
                            
                            reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Go to Sentry', url=message_profile[0]['href'])]])
                            
                            bot.send_message(
                                chat_id=chat['id'],
                                text=text,
                                reply_markup=reply_markup
                            )

                            logging.info(f"Email {msg.obj['Message-Id']} was sent to chat {chat['id']}")

                            with open('email_list.txt', 'a') as f:
                                f.write(msg.obj['Message-Id'] + ',')
        time.sleep(3)
