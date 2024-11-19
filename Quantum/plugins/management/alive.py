import asyncio
from platform import python_version as pyver
from pyrogram.enums import ChatType
from Quantum import app
from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ParseMode

from Quantum.utils.database import get_served_chats, get_served_users, add_served_user
from config import SUPPORT_CHAT, OWNER_ID,START_IMG_URL

async def member_permissions(chat_id: int, user_id: int):
    perms = []
    member = (await app.get_chat_member(chat_id, user_id)).privileges
    if not member:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_video_chats:
        perms.append("can_manage_video_chats")
    return perms

PHOTO = [
    "https://telegra.ph/file/d2a23fbe48129a7957887.jpg",
    "https://telegra.ph/file/ddf30888de58d77911ee1.jpg",
    "https://telegra.ph/file/268d66cad42dc92ec65ca.jpg",
    "https://telegra.ph/file/13a0cbbff8f429e2c59ee.jpg",
    "https://telegra.ph/file/bdfd86195221e979e6b20.jpg",
]


@app.on_message(filters.command("alive"))
async def restart(client, m: Message):
    bot = await app.get_me()
    btn = [
        [
            InlineKeyboardButton(text="ɴᴏᴏʙ", user_id=OWNER_ID),
            InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
        [
            InlineKeyboardButton(
                text="➕ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
    ]
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.2)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    owner=await app.get_users(OWNER_ID)
    await m.reply_photo(
        START_IMG_URL,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{bot.first_name}](f"t.me/{bot.username}")』**
  ━━━━━━━━━━━━━━━━━━━
    » **ᴍʏ ᴏᴡɴᴇʀ :** {owner.mention()}
  
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
   ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(btn),
        parse_mode=ParseMode.MARKDOWN
    )

@app.on_message(group=1)
async def save_statss(_, m):
    try:
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        if m.chat.type == ChatType.PRIVATE:
            served_users(m.from_user.id)
        elif m.chat.type==ChatType.SUPERGROUP:
            served_chats(m.chat.id)
        else:
            served_chats(m.chat.id)        

    except Exception as e:
        pass
