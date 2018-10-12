import telegram
import json
from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler
)
from emoji import emojize


class Post(object):

    def __init__(self):
        self.location = None
        self.photo = None

    def clean(self):
        self.location = None
        self.photo = None

    def save(self):
        data = {
            'location': {
                'latitude': self.location.latitude,
                'longitude': self.location.longitude
            },
            'photo': self.photo
        }

        with open('data.json', 'r') as file:
            file_data = json.load(file)

        file_data['data'].append(data)

        with open('data.json', 'w') as file:
            file.write(json.dumps(file_data))


post = Post()


def start(bot, update):

    msg = "Olá, sou o Vulture Bot."

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )


def support(bot, update):
    """
        Shows a help message.
    """

    msg = "Alguma mensagem de suporte."

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )


def get_photo(bot, update, post=post):
    msg = "Certo, agora preciso que envie a localização de onde foi tirada a foto."

    post.photo = update.message.photo[-1].file_id

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )


def get_location(bot, update, post=post):
    msg = "Pronto, a foto e a localização estão registrados, "
    msg += "obrigado por colaborar! "
    msg += emojize(':smile:', use_aliases=True)

    if post.photo:
        post.location = update.message.location
        post.save()
        post.clean()

        bot.send_message(
            chat_id=update.message.chat_id,
            text=msg,
            parse_mode=telegram.ParseMode.MARKDOWN
        )

        msg = "Seu registro será avaliado logo logo! E não se esqueça, dirija com cuidado e pare o veículo para os animais."
        msg += emojize(':innocent:', use_aliases=True)
        bot.send_message(
            chat_id=update.message.chat_id,
            text=msg,
            parse_mode=telegram.ParseMode.MARKDOWN
        )
    else:
        msg = "Ops! Preciso que envie uma foto antes da localização para que eu possa registrar corretamente."
        bot.send_message(
            chat_id=update.message.chat_id,
            text=msg,
            parse_mode=telegram.ParseMode.MARKDOWN
        )


def default(bot, update):
    """
        A default message to unknown command messages.
    """
    msg = "Desculpe, não entendi sua mensagem."
    msg += emojize(':pensive:', use_aliases=True)

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('support', support)
photo_handler = MessageHandler(Filters.photo, get_photo)
location_handler = MessageHandler(Filters.location, get_location)
default_handler = MessageHandler(Filters.command, default)
