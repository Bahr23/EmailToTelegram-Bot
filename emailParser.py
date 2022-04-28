import imaplib
import email
from bs4 import BeautifulSoup
from config import *


def get_last_messages():

    mail = imaplib.IMAP4_SSL(IMAP4_SERVER)
    mail.login(EMAIL_LOGIN, EMAIL_PASSWOARD)
    
    mail.list()
    mail.select("inbox")

    result, data = mail.search(None, "ALL")
    
    ids = data[0]
    id_list = ids.split()

    response = []

    for email_id in id_list[-10:]:
        result, data = mail.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        if email.utils.parseaddr(email_message['From'])[1] == FROM_EMAIL:
            response.append(email_message)

    return response


def get_link_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.find_all("a", {"style": "color:#4674ca;font-size:16px;font-weight:600;margin-right:10px;text-decoration:none"})
