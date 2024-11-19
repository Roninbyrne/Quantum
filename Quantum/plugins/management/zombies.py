from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid
from pyrogram.types import ChatPermissions
import asyncio
from Quantum import app
from Quantum.utils.decorators.permissions import adminsOnly

@app.on_message(filters.command("zombies") &~ filters.private)
@adminsOnly("can_restrict_members")
async def rm_deletedacc(client, message):
    del_u = 0
    del_status = "Group cleaned, 0 deleted accounts found."


    memek = await message.reply("Removing deleted accounts...")

    participants = []
    async for member in client.get_chat_members(message.chat.id):
        participants.append(member)

    for user in participants:
        if user.user.is_deleted:
            try:
                await client.ban_chat_member(message.chat.id, user.user.id)
                await client.unban_chat_member(message.chat.id, user.user.id)
                del_u += 1  # Increment only on successful removal
            except ChatAdminRequired:
                return await memek.edit("I do not have permission to ban members in this group.")
            except UserAdminInvalid:
                # This error is usually due to the user being an admin, so we don't count them
                pass
            await asyncio.sleep(1)

    if del_u > 0:
        del_status = f"Cleaned {del_u} Deleted account(s)."
    else:
        del_status = "No deleted accounts to clean."

    await memek.edit(del_status)

help_text = """
*ʀᴇᴍᴏᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs*
❍ /zombies : starts searching for deleted accounts in the group.
❍ /zombies clean : removes the deleted accounts from the group.
"""

mod_name = "Zᴏᴍʙɪᴇ"
