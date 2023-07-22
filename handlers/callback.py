from controllers.channel import delete_channel
from views.admin import AdminView
from config import admin_chat_id
from bot import bot

admin_view = AdminView()

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call) :
    print(call)
    if call.data.startswith('delete') :
        id = int(call.data.split(' ')[1])
        print(id)
        delete_channel(id=id)
        bot.send_message(chat_id=admin_chat_id,
                         text="The channel deleted successfully",
                         reply_markup=admin_view.delete_channel())
        
