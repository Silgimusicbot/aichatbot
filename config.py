from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ))
API_HASH = getenv("API_HASH", )
OWNER_ID = int(getenv("OWNER_ID", ))
STRING_SESSION = getenv("STRING_SESSION", "")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://shikhar:shikhar@cluster0.6xzlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUPPORT_GRP = getenv("SUPPORT_GRP", "aitsupport")
UPDATE_CHNL = getenv("UPDATE_CHNL", "aitbots")
OWNER_USERNAME = getenv("OWNER_USERNAME", "atondusalamde")

# Random Start Images
IMG = [
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
]


# Random Stickers
STICKER = [
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
]


EMOJIOS = [
    "😍",
    "🌹",
    "😔",
    "❤️",
    "😻",
    "😝",
    "😁",
    "👀",
    "🇦🇿",
    "🤣",
    "🙈",
    "🤨",
    "🥹",
]
