# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
from Quantum import app



@app.on_message(
    filters.command(["echo"], prefixes=["+", "/", "-", "?", "$", "&", "."] )
)
async def echo_(_, m):
    await m.delete()

    text = m.text.split(' ',1)[1]
    if m.reply_to_message:
        await m.reply_text(text,quote=True,reply_to_message_id=m.reply_to_message.id)
    else:
        await m.reply_text(text)
        