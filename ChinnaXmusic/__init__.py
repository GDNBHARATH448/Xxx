from ChinnaXmusic.core.bot import Aviax
from ChinnaXmusic.core.dir import dirr
from ChinnaXmusic.core.git import git
from ChinnaXmusic.core.userbot import Userbot
from ChinnaXmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
