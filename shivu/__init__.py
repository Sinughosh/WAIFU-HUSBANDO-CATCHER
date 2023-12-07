import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = 6550000741
sudo_users = ["6550000741", "5054912509"]
GROUP_ID = -1002028197914
TOKEN = ""
mongo_url = ""
PHOTO_URL = ["https://telegra.ph/file/294ba8e235a9932b69a86.jpg", "https://telegra.ph/file/294ba8e235a9932b69a86.jpg"]
SUPPORT_CHAT = "Grab_Your_Characters_6"
UPDATE_CHAT = "Guess_You_Caracter_v1"
BOT_USERNAME = "Grab_Your_Waifu_ixbot"
CHARA_CHANNEL_ID = -1001873432374
api_id = 20967639
api_hash = "f0cc55917e860f93d2c9aaa4a7caa69c"


application = Application.builder().token(TOKEN).build()
shivuu = Client("Shivu", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']



