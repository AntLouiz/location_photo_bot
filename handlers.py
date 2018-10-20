import telegram
from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler
)
from emoji import emojize
from post import Post


users_posts = {}


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


def get_photo(bot, update):
    chat_id = update.message.chat_id
    msg = "Certo, agora preciso que envie a localização de onde foi tirada a foto."

    if chat_id not in users_posts.keys():
        users_posts[chat_id] = Post()

    user_post = users_posts[chat_id]

    user_post.photo = update.message.photo[-1].file_id

    bot.send_message(
        chat_id=chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )


def get_location(bot, update):
    chat_id = update.message.chat_id
    msg = "Pronto, a foto e a localização estão registrados, "
    msg += "obrigado por colaborar! "
    msg += emojize(':smile:', use_aliases=True)
    error_msg = "Ops! Preciso que envie uma foto antes da localização para que eu possa registrar corretamente."

    if chat_id not in users_posts.keys():
        bot.send_message(
            chat_id=chat_id,
            text=error_msg,
            parse_mode=telegram.ParseMode.MARKDOWN
        )

        return False
    else:
        user_post = users_posts[chat_id]

    if user_post.photo:
        user_post.location = update.message.location
        user_post.save()
        del users_posts[chat_id]

        bot.send_message(
            chat_id=chat_id,
            text=msg,
            parse_mode=telegram.ParseMode.MARKDOWN
        )

        msg = "Seu registro será avaliado logo logo! E não se esqueça, dirija com cuidado e pare o veículo para os animais."
        msg += emojize(':innocent:', use_aliases=True)
        bot.send_message(
            chat_id=chat_id,
            text=msg,
            parse_mode=telegram.ParseMode.MARKDOWN
        )
    else:
        bot.send_message(
            chat_id=chat_id,
            text=error_msg,
            parse_mode=telegram.ParseMode.MARKDOWN
        )

        return False


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
