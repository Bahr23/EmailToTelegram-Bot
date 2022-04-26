import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import ConversationHandler

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
        else:
            text = 'Ошибка аторизации.'
    else:
        text = "Используйте /start [password]"
     
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


def help(update, context):
    if update.message.from_user.id in context.bot_data['auth-users']:
        text = '<code>/chats</code> - посмотреть список активных чатов.\n' \
                '<code>/chatinit</code> - добавить новый чат.\n' \
                '<code>/delchat</code> - удалить чат.'
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )


def all_messages(update, context):
    if update.message.from_user.id in context.bot_data['auth-users']:
        text = "Я не знаю как на это ответить. Воспользуйтесь разделом 'Помощь' (/help)"
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )


def chat_init(update, context):
    if update.message.from_user.id in context.bot_data['auth-users']:
        if context.args:
            subject = ' '.join(context.args)
            response = add_chat(subject, update.effective_chat.id)

            if response:
                text = 'Чат успешно добавлен'
            else:
                text = 'Используйте /chat_init [email subject] в канале'
            
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text,
            )


def my_chats(update, context):
    if update.message.from_user.id in context.bot_data['auth-users']:
        if update.effective_chat.id > 0:
            text = '<b>Активные чаты</b>\n'
            text = get_chats()
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text,
            )


def del_chat(update, context):
    if update.message.from_user.id in context.bot_data['auth-users']:
        if update.effective_chat.id > 0:
            if context.args and remove_chat(context.args[0]):
                text = 'Чат успешно удален'
            else:
                text = 'Используйте /delchat [chat_id]'
            
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text,
            )