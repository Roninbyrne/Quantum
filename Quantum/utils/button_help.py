from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import *
from random import choice
from Quantum import app


HELP = [
    [
        IKB("Aɪ", callback_data="HELP_AI"),
        IKB("Aғᴋ", callback_data="HELP_AFK"), 
        IKB("Cᴀʀʙᴏɴ", callback_data="HELP_CARBON"),
        
    ],
       [ IKB("Cᴏᴅᴇ Rᴜɴɴᴇʀ", callback_data="HELP_CODE"),
        IKB("Cᴏᴜᴘʟᴇ", callback_data="HELP_COUPLE"),
        IKB("Dᴏᴡɴʟᴏᴀᴅ", callback_data="HELP_DOWNLOAD"),
        
        
    ],
    [
       
        IKB("Eɴᴄʀʏᴘᴛ", callback_data="HELP_ENCRYPT"),
        IKB("Eɴɢʟɪsʜ", callback_data="HELP_ENGLISH"),
        IKB("Gᴀᴍᴇ", callback_data="HELP_GAME"), 
        
    ],
    [
         IKB("ɪɴғᴏ", callback_data="HELP_INFO"),
        IKB("ɪɴʟɪɴᴇ", switch_inline_query_current_chat=""),
        IKB("Kᴀʀᴍᴀ", callback_data="HELP_KARMA"),
        
        
    ],
    [
        IKB("ʟᴏɢᴏ", callback_data="HELP_LOGO"),
        IKB("Nᴇᴡs", callback_data="HELP_NEWS"),
        IKB("Qᴜᴏᴛᴇ", callback_data="HELP_QUOTE"),
        
    ],
    [
       
        IKB("Rᴀɴᴅᴏᴍ", callback_data="HELP_RANDOM"),
        IKB("sʜᴏʀᴛᴇɴᴇʀ", callback_data="HELP_SHORTNER"),
        IKB("Sᴜᴅᴏ", callback_data="HELP_SUDO"),
        
        
        
    ],
    [
        IKB("sᴛɪᴄᴋᴇʀ", callback_data="HELP_STICKER"),
        IKB("ᴛᴇʟᴇɢʀᴀᴘʜ", callback_data="HELP_TELEGRAPH"),
        IKB("ᴛʀᴀɴsʟᴀᴛᴇ", callback_data="HELP_TRANS"),
        
        
    ],
    [
        IKB("Tᴏᴋᴇɴ", callback_data="HELP_TOKEN"),
        IKB("ᴛʀᴜᴛʜ ᴅᴀʀᴇ", callback_data="HELP_TRUTH"),
        IKB("Tᴏᴏʟs", callback_data="HELP_TOOLS"),
        
    ],
     [IKB(" Hᴏᴍᴇ ", callback_data="RETURN")]
]
x = ["❤️", "🎉", "✨", "🪸", " 🎉 ", " 🎈 ", "🎯"]
g = choice(x)


MAIN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{app.username}?startgroup=true",
        ),
    ],
    [
        IKB(text="ʜᴇʟᴘs", callback_data="HELP"),
    ],
    [
        IKB(text="sᴏᴜʀᴄᴇ ", callback_data="HELP_source"),
        
        IKB(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
]
]
IMGX = [
    [
        IKB(text="Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
        IKB(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
]
PNG_BTN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{app.username}?startgroup=true",
        ),
    ],
    [
        IKB("sᴜᴘᴘᴏʀᴛ",
            url=f"https://t.me/{SUPPORT_GRP}",
        ),
    ],
]


HELP_BACK = [

    [
        IKB("ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]
#  force
M =IKM( [
    [IKB(text="ᴄʟᴏsᴇ", callback_data="closeforce")]
])
ADD_ME= [
    [
        IKB(
        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{app.username}?startgroup=true",
        )
    ]]
VERIFY=  IKM([
    [
        IKB(
        "verify",
            url=f"https://t.me/{app.username}?start=true",
        )
    ]])
SOURCE_BUTTONS = IKM(
    [
        [IKB("sᴏᴜʀᴄᴇ", callback_data="HELP_hurr")],
        [
            IKB(" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
            IKB(text="ʙᴀᴄᴋ ", callback_data="RETURN")
        ]
    ]
)

