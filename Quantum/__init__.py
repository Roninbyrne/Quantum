from Quantum.core.bot import QuantX
from Quantum.core.dir import dirr

from Quantum.core.userbot import Userbot
from Quantum.misc import dbb, heroku

from .logging import LOGGER

dirr()
dbb()
heroku()

app = QuantX()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
