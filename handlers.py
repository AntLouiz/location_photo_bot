import telegram
from telegram.ext import (
    Filters,
    CommandHandler,
    RegexHandler,
    MessageHandler
)
from emoji import emojize
from decouple import config


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
default_handler = MessageHandler(Filters.command, default)
