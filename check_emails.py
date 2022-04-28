import time

from emailParser import *
from chatsMananger import *


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
                        
                            links = get_link_from_html(html)
                            
                            for l in links:
                                text += f"<a href='{l['href']}'>{l.text}</a>\n"
                            
                        
                            get_html_image(html)
                        
                        
                            in_file = open('temp/file.png', "rb")
                            photo_byte = in_file.read()
                            in_file.close()

                            # photo_byte = get_html_image(html)

                            bot.send_document(
                                chat_id=c['id'],
                                caption=text,
                                document=photo_byte,       
                            ) 
        time.sleep(3)