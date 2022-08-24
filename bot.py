#    This file is part of the ChannelAutoForwarder distribution (https://github.com/xditya/ChannelAutoForwarder).
#    Copyright (c) 2021 Adiya
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/xditya/ChannelAutoForwarder/blob/main/License> .

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    datgbot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await datgbot(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hi `{ok.user.first_name},`\n\n**I am a channel auto forward bot. \n\n /About to know more.**", buttons=[Button.url("🤖 Updates", url="https://t.me/movievillachat"), Button.url("♥️ Source", url="https://youtube.com/channel/UCAjLSt8ARs8e9AX014hoJtQ")], link_preview=False)


@datgbot.on(events.NewMessage(pattern="/About"))
async def helpp(event):
    await event.reply("➜  𝙲𝚁𝙴𝙰𝚃𝙾𝚁:  [𝐍𝐚𝐧𝐜𝐲](https://t.me/nancyji_bot) \n➜  𝙲𝙷𝙰𝙽𝙽𝙴𝙻:  [𝐌𝐨𝐯𝐢𝐞 𝐕𝐢𝐥𝐥𝐚](https://t.me/MovieVilla99) \n➜  𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴:  𝙿𝚈𝚃𝙷𝙾𝙽 𝟹 \n➜  𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴:  𝙼𝙾𝙽𝙶𝙾 𝙳𝙱 \n➜  𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁:  𝙷𝙴𝚁𝙾𝙺𝚄 \n➜  𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂:  v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"), link_preview=False)


@datgbot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                await datgbot.send_file(tochnl, photo, caption = event.text, link_preview = False)
            elif event.media:
                try:
                    if event.media.webpage:
                        await datgbot.send_message(tochnl, event.text, link_preview = False)
                        return
                except:
                    media = event.media.document
                    await datgbot.send_file(tochnl, media, caption = event.text, link_preview = False)
                    return
            else:
                await datgbot.send_message(tochnl, event.text, link_preview = False)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
print("Do visit @MovieVilla99..")
datgbot.run_until_disconnected()
