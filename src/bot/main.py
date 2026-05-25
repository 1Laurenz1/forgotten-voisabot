import asyncio

from pyrogram.errors import RPCError

from .client import client as app
from src.utils.web_app_data import get_web_app_data
from src.logger.logger_main import logger


async def main() -> None:
    logger.info("Starting Telegram client...")

    try:
        await app.start()

        logger.debug("Telegram client started successfully")

        web_app_data = await get_web_app_data(app)

        logger.debug("tgWebAppData received successfully")

        logger.info(
            "\nYOUR TELEGRAM WEBAPP DATA:\n"
            f"{web_app_data}"
        )

    except RPCError as e:
        logger.exception(
            f"Telegram RPC error occurred: {str(e)}"
        )

    except Exception as e:
        logger.exception(f"Unexpected error occurred: {e}")

    finally:
        logger.debug("Stopping Telegram client...")

        try:
            await app.stop()
        except Exception:
            pass


if __name__ == "__main__":
    asyncio.run(main())
