import telegram
from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler
)
from emoji import emojize
from decouple import config


class Post(object):

  def __init__(self):
    self.location = None
    self.photo = None

  def clean(self):
    self.location = None
    self.photo = None

  def save(self):
    print(self.location)
    print(self.photo)


post = Post()

def start(bot, update):

    msg = "Olá, sou o Bot Karnissa."

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
  post.photo = update.message.photo[-1].file_id


def get_location(bot, update, post=post):

  if post.photo:
    post.location = update.message.location
    post.save()
    post.clean()


def default(bot, update):

  """
    A default message to unknown command messages.
  """

  msg = "Desculpe, nao entendi sua mensagem."
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
