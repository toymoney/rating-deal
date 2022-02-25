from telethon.sync import TelegramClient, events
import asyncio
import pyrogram

api_id = 1655877
api_hash = '409cdce961fea4a8ba3381f0bb15d9e1'


groups = [-1444746721,-1554041120,-1320270732,
          -1418787216,-1152662392,-1554041120,-1502476123,
          -1539767170,-1408267999,-1159961237,-1233150161,
          -1776776044,-1577844824,-1581385213,-1461051167,905622039]

group_list = []
  
for group_list in groups:
 lists = group_list

  
word = 'rating'
word1=''

for i in word:
  if (i.isupper())==True:
    word1+=(i.lower())
    
client = TelegramClient('anon', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
  chat = await event.get_chat()
  chat_id = event.chat_id  
  if chat_id == group_list:
      msg = event.raw_text
      if word1 in msg:
              await client.send_message(-791450034, event.raw_text)

client.start()
client.run_until_disconnected()
