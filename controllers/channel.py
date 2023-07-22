from dependencies.database import get_session
from models.channel import Channel
from sqlmodel import select

def get_channels() : 
    sess = next(get_session())
    return sess.exec(select(Channel)).all()

def delete_channel(id) : 
    sess = next(get_session())
    channel = sess.get(Channel,id)
    if channel : 
        sess.delete(channel)
        sess.commit() 

def add_channel(name,channel_id) : 
    sess = next(get_session())
    channel = Channel(
        name=name,
        channel_id=int("-100"+channel_id.strip())
    )
    sess.add(channel)
    sess.commit()