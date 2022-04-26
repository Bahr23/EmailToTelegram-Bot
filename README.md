# EmailToTelegram Bot

## Установка

1. Установите все необходимые зависимости `pip install -r requirements.txt`.
2. Заполните config.py.

    ```python

    # Bot
    TOKEN = '' # Апи токен, полученный в @BotFather
    PASSWORD = 'root' # Пароль для доступа к боту

    # Email settings

    IMAP4_SERVER = 'imap.yandex.com' # IMAP4_SERVER, оставьте так для Яндекс почты
    EMAIL_LOGIN = '' # Логин для почты от куда парсить письма
    EMAIL_PASSWOARD = '' # Пароль для почты от куда парсить письма

    FROM_EMAIL = '' # Почта отправителя
    ```

    >`TOKEN` получаем в [@BotFather](https://t.me/BotFather) с помощью команды /newbot.

3. Запустите файл `main.py` с помощью `.../emailBot/ python main.py`.
