from pyrogram import Client
from pyrogram.raw.functions.contacts import ResolveUsername
from pyrogram.raw.types import InputPeerUser, InputUser
from pyrogram.raw.functions.messages import RequestMainWebView

from src.config.config_reader import settings
from src.logger.logger_main import logger

from urllib.parse import unquote


async def get_web_app_data(app: Client) -> str:
    resolved = await app.invoke(
        ResolveUsername(username=settings.BOT_USERNAME)
    )
    bot = resolved.users[0]
    
    bot_peer = InputPeerUser(
        user_id=bot.id,
        access_hash=bot.access_hash,
    )
    bot_user = InputUser(
        user_id=bot.id,
        access_hash=bot.access_hash,
    )
    
    result = await app.invoke(
        RequestMainWebView(
            peer=bot_peer,
            bot=bot_user,
            platform="web"
        )
    )
    
    logger.debug("tgWebAppData received successfully")

    url = result.url
    data = url.split("tgWebAppData=")[1].split("&tgWebAppVersion")[0]
    data = unquote(unquote(data))
    
    return data
