import logging 
import time
from Abg import patch
 
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from pyrogram.enums import ParseMode

import config

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)
boot = time.time()
mongo = MongoCli(config.MONGO_URL)
db = mongo.Anonymous
OWNER = config.OWNER_ID

class Rzayev(Client):
    def __init__(self):
        super().__init__(
            name="Rzayev",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="az",
            session_string=config.STRING_SESSION,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
            bot_token="7404664253:AAEOrGB6_ZjQ0QmCONq9jML4H32Ew31OcDo"
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()


Rzayev = Rzayev()
