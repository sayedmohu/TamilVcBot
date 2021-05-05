# import logging
from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED by @sayedmohu')
idle()
app.stop()
print('\n>>> USERBOT STOPPED by @sayedmohu')

