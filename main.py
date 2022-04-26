import logging

from telegram import Bot, ParseMode
from telegram.ext import Updater, Defaults

from config import *
from handlers import command_handler
from check_emails import last_email
from threading import Thread

def main():

    defaults = Defaults(parse_mode=ParseMode.HTML)
    bot = Bot(token=TOKEN, defaults=defaults)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(token=TOKEN, defaults=defaults)
    dispatcher = updater.dispatcher

    command_handler(dispatcher)

    updater.start_polling()


    th = Thread(target=last_email(bot))
    th.start()


    updater.idle()


if __name__ == "__main__":
    main()
