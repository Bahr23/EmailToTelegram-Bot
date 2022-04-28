import time

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from emailParser import *
from chatsMananger import *
from htmlParser import *


def last_email(bot):
    while True:

        messages = get_last_messages()

        if messages:
            chats = get_data()
            for message in messages:
                for c in chats:
                    if c['subject'] in message['Subject']:
                        with open('email_list.txt', 'r') as f:
                            email_list = f.read().split(',')
                        
                        if message['Message-id'] not in email_list:
                            
                            with open('email_list.txt', 'a') as f:
                                f.write(message['Message-Id'] + ',')
                            
                            text = ''
                            html = message.get_payload(decode=True).decode('utf-8')

                            msg = get_message_profile(html)

                            text = f"<b><a href='{msg['main-link']['href']}'>{msg['main-link']['text']}</a></b>" \
                                   f"\n\n<b>Exception</b>\n<code>{msg['Exception']}</code>"
                            if 'Request' in msg.keys():
                                text += f"\n\n<b>Request</b>\n<i>URL</i> <a href='{msg['Request']['URL']['href']}'>" \
                                   f"{msg['Request']['URL']['text']}</a>"
                                if 'Query' in msg['Request'].keys():
                                   text += f"\n<i>Query</i> <code>{msg['Request']['Query']}</code>"
                            if 'User' in msg.keys():
                                text += f"\n\n<b>User</b>\n<i>IP Address:</i> <code>{msg['User']}</code>"\

                            print(text)

                            reply_markup = InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="Go to Sentry", url=msg['main-link']['href'])]
                            ])

                            bot.send_message(
                                chat_id=c['id'],
                                text=text,
                                reply_markup=reply_markup
                            )
        time.sleep(3)
