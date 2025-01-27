import time
from pyrogram import filters
from pyrogram.types import Message
from Mikasa import app
from Mikasa.database import add_afk, is_afk, remove_afk

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@app.on_message(filters.command(["afk", f"afk@{app.username}"]))
async def active_afk(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    verifier, reasondb = await is_afk(user_id)

    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time(int(time.time() - timeafk))
            if afktype == "text":
                await message.reply_text(
                    f"{message.from_user.first_name} ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
                    disable_web_page_preview=True,
                )
            if afktype == "text_reason":
                await message.reply_text(
                    f"{message.from_user.first_name} ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nRᴇᴀsᴏɴ: `{reasonafk}`",
                    disable_web_page_preview=True,
                )
        except Exception as e:
            await message.reply_text(
                f"**{message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ.",
                disable_web_page_preview=True,
            )
        return

    if len(message.command) == 1 and not message.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and not message.reply_to_message:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(message.command) > 1 and message.reply_to_message.sticker:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_afk(user_id, details)
    await message.reply_text(
        f"{message.from_user.first_name} ɪs ɴᴏᴡ ᴀғᴋ.!"
    )

@app.on_message(filters.all)
async def afk_check_message(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    verifier, reasondb = await is_afk(user_id)

    if verifier:
        await remove_afk(user_id)
        seenago = get_readable_time(int(time.time() - reasondb["time"]))
        reasonafk = reasondb.get("reason", "No reason provided")
        await message.reply_text(
            f"{message.from_user.first_name} ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}.\n\nReason: {reasonafk}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.reply)
async def afk_reply_check(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.reply_to_message.from_user.id
    verifier, reasondb = await is_afk(user_id)
    if verifier:
        seenago = get_readable_time(int(time.time() - reasondb["time"]))
        reasonafk = reasondb.get("reason", "No reason provided")
        await message.reply_text(
            f"{message.reply_to_message.from_user.first_name} is currently AFK and was away for {seenago}.\n\nReason: {reasonafk}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.mentioned)
async def afk_mention_check(_, message: Message):
    if message.sender_chat:
        return
    mentioned_users = message.entities
    if mentioned_users:
        for entity in mentioned_users:
            if entity.type == "mention":
                mentioned_user_id = message.text[entity.offset:entity.offset + entity.length].strip('@')
                user = await app.get_users(mentioned_user_id)
                verifier, reasondb = await is_afk(user.id)
                if verifier:
                    seenago = get_readable_time(int(time.time() - reasondb["time"]))
                    reasonafk = reasondb.get("reason", "No reason provided")
                    await message.reply_text(
                        f"{user.first_name} is currently AFK and was away for {seenago}.\n\nReason: {reasonafk}",
                        disable_web_page_preview=True,
                    )