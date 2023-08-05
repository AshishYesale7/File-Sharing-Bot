#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6430326857:AAE5Bt-9IXUdctWXbseV2kp1D8rGpnwBT0U")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "14757820"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "aca345115e9be874c232de0a62c8f621")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001912535408"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1559570895"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hyper4stream:ashishvy@cluster0.i8vytdk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{filename}")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot! \n\n <b>\n○ Download Movie App : <a href='https://hyperstream.page.link/HyperStreamWeb'> DOWNLOAD </a>\n\n○ Video Player : <a href='https://hstream.page.link/player'> Download</a>\n\n○ Channel : @h_stream_app\n\n○ Support Group : @h_stream_group</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1559570895)

LOG_FILE_NAME = "filesharingbot.txt"
  
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
