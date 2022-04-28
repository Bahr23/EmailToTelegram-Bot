import imaplib
import email
from html2image import Html2Image
from bs4 import BeautifulSoup
from config import *
from PIL import Image
import io


def get_html_image(html):
    try:
        hti = Html2Image(output_path='temp')
        im = Image.open(hti.screenshot(html_str=html, size=(800, 1500))[0])
        box = (10, 100, im.width-10, im.height)
        crop = im.crop(box)
    except Exception as e:
        print(e)
    return crop.save('temp/file.png', 'png')

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
