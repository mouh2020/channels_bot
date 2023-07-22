from bot import bot
from config import admin_chat_id
from views.admin import AdminView

admin_view = AdminView()

def message_handler(message) : 
    if message.text == "Add Channel" :
        bot.send_message(chat_id=admin_chat_id,
                         text="Please enter the name of the channel you want to add ",
                         reply_markup=admin_view.back_home()) 
        bot.register_next_step_handler(message,admin_view.add_channel_name)
        return True
    if message.text == "Delete Channel" :
        bot.send_message(chat_id=admin_chat_id,
                         text="Choose the channel you want to delete.",
                         reply_markup=admin_view.delete_channel()) 
        return True
    elif message.text  == "Send Message" : 
        bot.send_message(chat_id=admin_chat_id,
                         text="Please enter the message you want to send to channels ",
                         reply_markup=admin_view.back_home()) 
        bot.register_next_step_handler(message,admin_view.send_message)
        return True
    elif message.text  == "Back Home" :
        bot.send_message(chat_id=admin_chat_id,
                            text="Admin Home Panel",
                            reply_markup=admin_view.home())
        return True
    else : 
        bot.send_message(chat_id=admin_chat_id,
                            text="Admin Home Panel",
                            reply_markup=admin_view.home())
