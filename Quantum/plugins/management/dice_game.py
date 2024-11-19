
from pyrogram import  filters
#from config import *
from Quantum import app as mukesh



@mukesh.on_message(filters.command("dice"))
async def dice(bot, message):
   # await bot.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
  
@mukesh.on_message(filters.command("dart"))
async def dart(bot, message):
   # await bot.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)

@mukesh.on_message(filters.command("basket"))

async def basket(bot, message):
    #await bot.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
@mukesh.on_message(filters.command("jackpot"))
async def basket(bot, message):
   # await bot.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
@mukesh.on_message(filters.command("ball"))
async def basket(bot, message):
   # await bot.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
@mukesh.on_message(filters.command("football"))
async def basket(bot, message):
  #  await bot.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
__help__ = """
*ᴘʟᴀʏ ɢᴀᴍᴇ ᴡɪᴛʜ ᴇᴍᴏᴊɪꜱ*
❍ /dice - Dice 🎲
❍ /dart - Dart 🎯
❍ /basket - Basket Ball 🏀
❍ /ball - Bowling Ball 🎳
❍ /football - Football ⚽
❍ /jackpot - Spin slot machine 🎰

*ғᴀᴋᴇ ᴀɴɪᴍᴀᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅ*
 ❍ /love - ᴜsᴇ ɪᴛ ɪғ ᴜ ʜᴀᴠᴇ ɢɪʀʟғʀɪᴇɴᴅ
 ❍ /hack -  ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ
 ❍ /moon    - ᴛᴏ ᴡɪsʜ ɢɴ ᴛᴏ ᴜʀ ʟᴏᴠᴇ
 ❍ /kill  -  ᴛᴏ ᴋɪʟʟ  ᴜʀ ɢғ ᴅᴀᴅ
 ❍ /bombs -  ᴛᴏ sᴜᴄɪᴅᴇ ᴜʀsᴇʟғ
 ❍ /police - ᴛᴏ ᴄᴀʟʟ ᴍᴀsᴛᴇʀᴍɪɴᴅ ᴘᴏʟɪᴄᴇ
"""
__mod_name__ = "ɢᴀᴍᴇ"