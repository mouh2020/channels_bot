from bot import bot
from telebot.types import Message
from database import create_db_and_tables
from handlers.message import message_handler
from config import admin_chat_id
from handlers.callback import *
from dependencies.auth import admin_authenticated

@bot.message_handler(func=lambda message:True)
def all_messages(message : Message) :
    try : 
        if admin_authenticated(message.from_user.id) :
            print(message.text)
            message_handler(message=message)
    except Exception as e : 
        bot.send_message(message.from_user.id,
                         f"Error occured {str(e)}")

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()