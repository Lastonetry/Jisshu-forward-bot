import os
from config import Config

class Translation(object):
  START_TXT = """<b>ʜᴇʟʟᴏ {}</b>

<i>ɪ'ᴍ ᴀ <b>ᴘᴏᴡᴇʀғᴜʟʟ</b> ᴀᴜᴛᴏ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ

ɪ ᴄᴀɴ ғᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ</i> <b>➜ ᴡɪᴛʜ ᴍᴀɴʏ ғᴇᴀᴛᴜʀᴇs.
ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ</b>

<b>👨🏼‍💻 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: <a href='https://t.me/KingMogger'>ᴋɪɴɢ ᴍᴏɢɢᴇʀ</a>🥀</b>"""


  HELP_TXT = """<b><u>🔆 ʜᴇʟᴘ</b></u>

<u>**📚 Available commands:**</u>
<b>⏣ __/start - check I'm alive__ 
⏣ __/forward - forward messages__
⏣ __/unequify - delete duplicate messages in channels__
⏣ __/settings - configure your settings__
⏣ __/reset - reset your settings__</b>

<b><u>💢 Features:</b></u>
<b>► __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission__
► __Forward message from private channel to your channel by using userbot(user must be member in there)__
► __custom caption__
► __custom button__
► __support restricted chats__
► __skip duplicate messages__
► __filter type of messages__
► __skip messages based on extensions & keywords & size__</b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
<b>► __add a bot or userbot__
► __add atleast one to channel__ `(your bot/userbot must be admin in there)`
► __You can add chats or bots by using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
► __Then use /forward to forward messages__</b>"""
  
  ABOUT_TXT = """<b>╭──────❰ 🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs ❱──────〄
│ 
│ 🤖 ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/rForwardxbot>ғᴏʀᴡᴀʀᴅ ʙᴏᴛ</a>
│ 👨‍💻 ᴅᴇᴠᴘʟᴏᴇʀ : <a href=https://t.me/KingMogger>ᴋɪɴɢ ᴍᴏɢɢᴇʀ</a>
│ 📡 ʜᴏsᴛᴇᴅ ᴏɴ : <a href=https://www.hetzner.com/>ʜᴇᴛᴢɴᴇʀ</a>
│ 🗣️ ʟᴀɴɢᴜᴀɢᴇ  : <a href=https://www.python.org/>ᴘʏᴛʜᴏɴ 3 
{python_version}</a>
│ 📚 ʟɪʙʀᴀʀʏ  : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>  
╰────────────────────⍟</b>"""
  
  STATUS_TXT = """<b>╭──────❪ 🤖 ʙᴏᴛ sᴛᴀᴛᴜs ❫─────⍟
│
├👨 ᴜsᴇʀs  : {}
│
├🤖 ʙᴏᴛs : {}
│
├📣 ᴄʜᴀɴɴᴇʟ  : {} 
╰───────────────────⍟</b>""" 
  
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """<b>╭────❰ <u>ғᴏʀᴡᴀʀᴅɪɴɢ sᴛᴀᴛᴜs...</u> ❱────❍
┃
┣⊸<b>🕵 ғᴇᴄʜᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>✅ sᴜᴄᴄᴇғᴜʟʟʏ ғᴡᴅ :</b> <code>{}</code>
┣⊸<b>👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🗑️ ᴅᴇʟᴇᴛᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🪆 sᴋɪᴘᴘᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>📊 sᴛᴀᴛᴜs  :</b> <code>{}</code>
┣⊸<b>⏳ ᴘʀᴏɢʀᴇss  :</b> <code>{}</code> %
┣⊸<b>⏰ ᴇᴛᴀ :</b> <code>{}</code>
┃
╰────⌊ <b>{}</b> ⌉───❍</b>"""

  TEXT1 = """<b>╭─❰ <u>ғᴏʀᴡᴀʀᴅɪɴɢ sᴛᴀᴛᴜs....</u> ❱─❍
┃
┣⊸🕵𝙁𝙚𝙘𝙝𝙚𝙙 𝙈𝙨𝙜 : {}
┣⊸✅𝙎𝙪𝙘𝙘𝙚𝙛𝙪𝙡𝙮 𝙁𝙬𝙙 : {}
┣⊸👥𝘿𝙪𝙥𝙡𝙞𝙘𝙖𝙩𝙚 𝙈𝙨𝙜: {}
┣⊸🗑𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝙈𝙨𝙜: {}
┣⊸🪆𝙎𝙠𝙞𝙥𝙥𝙚𝙙 : {}
┣⊸📊𝙎𝙩𝙖𝙩𝙨 : {}
┣⊸⏳𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 : {}
┣⊸𝙀𝙏𝘼 : {}
┃
╰─⌊ {} ⌉─❍</b>"""

  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DOUBLE_CHECK = """<b><u>ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋɪɴɢ ⚠️</b></u>
<code>ʙᴇғᴏʀᴇ ғᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ ᴍᴇssᴀɢᴇs, ᴄʟɪᴄᴋ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴏɴʟʏ ᴀғᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢs-</code>

<b>★ ʏᴏᴜʀ ʙᴏᴛ:</b> [{botname}](t.me/{botuname})
<b>★ ғʀᴏᴍ ᴄʜᴀɴɴᴇʟ:</b> `{from_chat}`
<b>★ ᴛᴏ ᴄʜᴀɴɴᴇʟ:</b> `{to_chat}`
<b>★ sᴋɪᴘ ᴍᴇssᴀɢᴇs:</b> `{skip}`

<i>[{botname}](t.me/{botuname}) ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ **ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ**</i> (`{to_chat}`)
<i>ɪғ ᴛʜᴇ **sᴏᴜʀᴄᴇ ᴄʜᴀᴛ** ɪs ᴘʀɪᴠᴀᴛᴇ, ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴍᴇᴍʙᴇʀ ᴏʀ ʏᴏᴜʀ ʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇʀᴇ ᴛᴏ ғᴏʀᴡᴀʀᴅ</b></i>

<b>ɪғ ᴛʜᴇ ᴀʙᴏᴠᴇ ɪs ᴄʜᴇᴄᴋᴇᴅ ᴛʜᴇɴ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴄᴀɴ ʙᴇ ᴄʟɪᴄᴋᴇᴅ</b>"""
