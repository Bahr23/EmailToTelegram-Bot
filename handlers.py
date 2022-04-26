import re

from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from user_commands import *


def command_handler(dispatcher):

    #-------- Commands --------

    # User commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("chatinit", chat_init))
    dispatcher.add_handler(CommandHandler("delchat", del_chat))
    dispatcher.add_handler(CommandHandler("chats", my_chats))


    # Utils
    dispatcher.add_handler(MessageHandler(Filters.text, all_messages))
