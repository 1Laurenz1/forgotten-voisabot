from pyrogram import Client

from src.config.config_reader import settings


client = Client(
    "forgotten-voisabot",
    api_id=settings.API_ID.get_secret_value(),
    api_hash=settings.API_HASH.get_secret_value(),
)
