from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8cfaf7f865fda4c567f3c.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/8cfaf7f865fda4c567f3c.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/l_DIGITAL_WORLD_l")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/l_RAGHAV_l")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6028744448").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
