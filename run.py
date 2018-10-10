from telegram.ext import Updater
from handlers import (
    start_handler,
    help_handler,
    photo_handler,
    location_handler,
    default_handler
)
from settings import TELEGRAM_BOT_TOKEN


def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(photo_handler)
    dispatcher.add_handler(location_handler)
    dispatcher.add_handler(default_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
