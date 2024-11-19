from gpytranslate import SyncTranslator
from pyrogram import filters 
from pyrogram.enums import ChatAction, ParseMode, ChatType
trans = SyncTranslator()
from Quantum import app
@app.on_message(filters.command("tr"))
async def totranslate(b,m):
    message =  m.text
    reply_msg = m.reply_to_message
    if not reply_msg:
        await m.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇs ᴏʀ ᴡʀɪᴛᴇ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴏᴛʜᴇʀ ʟᴀɴɢᴜᴀɢᴇs ғᴏʀ ᴛʀᴀɴsʟᴀᴛɪɴɢ ɪɴᴛᴏ ᴛʜᴇ ɪɴᴛᴇɴᴅᴇᴅ ʟᴀɴɢᴜᴀɢᴇ\n\n"
            "ᴇxᴀᴍᴘʟᴇ: `/tr en-hi` ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ғʀᴏᴍ ᴇɴɢʟɪsʜ ᴛᴏ ʜɪɴᴅɪ\n"
            "ᴏʀ ᴜsᴇ: `/tr en` ғᴏʀ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴅᴇᴛᴇᴄᴛɪᴏɴ ᴀɴᴅ ᴛʀᴀɴsʟᴀᴛɪɴɢ ɪᴛ ɪɴᴛᴏ ᴇɴɢʟɪsʜ.\n"
            """ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ sᴇᴇ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇsʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇs ғᴏʀ ᴛʀᴀɴsʟᴀᴛɪᴏɴ : af, am, ar, az, be, bg, bn, bs, ca, ceb, co, cs, cy, da, de, el, en, eo, es,
et, eu, fa, fi, fr, fy, ga, gd, gl, gu, ha, haw, hi, hmn, hr, ht, hu, hy, id, ig, is, it, iw, ja, jw, ka, kk, km, kn, ko, ku, ky, la, lb, lo, lt, lv, mg, mi, mk, ml, mn, mr, ms, mt, my, ne, nl, no, ny, pa, pl, ps, pt, ro, ru, sd, si, sk, sl, sm, sn, so, sq, sr, st, su, sv, sw, ta, te, tg, th, tl, tr, uk, ur, uz, vi, xh, yi, yo, zh, zh_CN, zh_TW, zu.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = trans.detect(to_translate)
            dest = args
    except IndexError:
        source = trans.detect(to_translate)
        dest = "en"
    translation = trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"<b>ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest}</b> :\n"
        f"<code>{translation.text}</code>"
    )

    await m.reply_text(reply, parse_mode=ParseMode.HTML)


