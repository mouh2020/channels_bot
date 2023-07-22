from telebot.types import *
from bot import bot
from config import admin_chat_id
import json
from utils.emojis import repalce_emojis
from dependencies.database import get_session
from models.channel import Channel
from sqlmodel import select
from controllers.channel import *

class AdminView : 

    def home(self) : 
        markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        row    = [KeyboardButton('Add Channel'),KeyboardButton('Delete Channel')]
        markup.add(*row)
        row    = [KeyboardButton('Send Message')]
        markup.add(*row)
        return markup
    
    def delete_channel(self) : 
        channels = get_channels()
        markup = InlineKeyboardMarkup()
        for channel in channels :
            markup.add(InlineKeyboardButton(text = channel.name,
                                            callback_data = f"delete {str(channel.id)}" ))
        return markup


    def send_message(self,message) : 
        if self.check_back(message=message.text) :
            return
        channels = get_channels()
        for channel in channels : 
            try :
                bot.send_message(chat_id=channel.channel_id,
                                text=repalce_emojis(message=message.text),
                                )
                bot.send_message(chat_id=admin_chat_id,
                                 text=f"successfully send to channel with id : {channel.name}")
            except Exception as e : 
                bot.send_message(chat_id=admin_chat_id,
                                 text=f"Unable to send to channel named : {channel.name}")      
        bot.send_message(chat_id=admin_chat_id,
                         text="Admin Home Panel",
                         reply_markup=self.home())        

    def add_channel_name(self,message) :
        if self.check_back(message=message.text)  : 
            return
        self.channel_name = message.text
        bot.send_message(chat_id=admin_chat_id,
                         text="Please enter the ID of the channel you want to add ") 
        bot.register_next_step_handler(message,self.add_channel_id)
    def add_channel_id(self,message) : 
        if self.check_back(message=message.text) : 
            return
        add_channel(name=self.channel_name,
                    channel_id=message.text)
        bot.send_message(chat_id=admin_chat_id,
                         text="Admin Home Panel",
                         reply_markup=self.home())      
        return
    def back_home(self) : 
        markup = ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        row    = [KeyboardButton('Back Home')]
        markup.add(*row)
        return markup
    
    def check_back(self,message) : 
        if message == "Back Home" : 
            bot.send_message(chat_id=admin_chat_id,
                             text="Admin Home Panel",
                             reply_markup=self.home())
            return True
        



    

