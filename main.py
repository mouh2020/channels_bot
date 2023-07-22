from bot import bot
from telebot.types import Message
from database import create_db_and_tables
from handlers.message import message_handler
from config import admin_chat_id
from handlers.callback import *


@bot.message_handler(func=lambda message:True)
def all_messages(message : Message) : 
    if message.from_user.id == admin_chat_id :
        print(message.text)
        message_handler(message=message)

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()