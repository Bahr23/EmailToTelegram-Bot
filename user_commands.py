from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import ConversationHandler
import logging
from chatsMananger import *


def start(update, context):
    if context.args:
        if context.args[0] == PASSWORD:
            text = 'Вы успешно авторизовались, используйте <code>/help</code> для получения списка команд.'
            if 'auth-users' in context.bot_data.keys():
                if update.message.from_user.id not in context.bot_data['auth-users']:
                    context.bot_data['auth-users'].append(update.message.from_user.id)
            else:
                context.bot_data['auth-users'] = [update.message.from_user.id]

            logging.info(f"User {update.message.from_user.id} loged in.")
        else:
            text = 'Ошибка аторизации.'
    else:
        text = "Используйте /start [password]"
     
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


def help(update, context):
    try:
        if update.message.from_user.id in context.bot_data['auth-users']:
            text = '<code>/chats</code> - посмотреть список активных чатов.\n' \
                    '<code>/chatinit</code> - добавить новый чат.\n' \
                    '<code>/delchat</code> - удалить чат.'
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text,
            )
    except:
        logging.info(f"User {update.message.from_user.id} is trying to access without authorization.")


def chat_init(update, context):
    if update.channel_post:
        args = update.channel_post.text.split(' ')[1:]
        if args:
            if args[0] == PASSWORD:
                subject = ' '.join(args[1:])
                response = add_chat(subject, update.channel_post.chat.id)

                if response:
                    text = 'Чат успешно добавлен'
                    logging.info(f"Chat {update.channel_post.chat.id} is added to chat list.")
                else:
                    text = 'Используйте /chatinit [password] [email subject] в канале'
                
                context.bot.send_message(
                    chat_id=update.channel_post.chat.id,
                    text=text,
                )



def all_messages(update, context):
    try:
        if update.message.from_user.id in context.bot_data['auth-users']:
            text = "Я не знаю как на это ответить. Воспользуйтесь разделом 'Помощь' (/help)"
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text,
            )
    except:
        logging.info(f"User {update.message.from_user.id} is trying to access without authorization.")


def my_chats(update, context):
    try:
        if update.message.from_user.id in context.bot_data['auth-users']:
            if update.effective_chat.id > 0:
                text = '<b>Активные чаты</b>\n'
                text = get_chats()
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=text,
                )
    except:
        logging.info(f"User {update.message.from_user.id} is trying to access without authorization.")


def del_chat(update, context):
    try:
        if update.message.from_user.id in context.bot_data['auth-users']:
            if update.effective_chat.id > 0:
                if context.args and remove_chat(context.args[0]):
                    text = 'Чат успешно удален'
                    logging.info(f"Chat {context.args[0]} is removed from chat list.")
                else:
                    text = 'Используйте /delchat [chat_id]'
                
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=text,
                )
    except:
        logging.info(f"User {update.message.from_user.id} is trying to access without authorization.")
