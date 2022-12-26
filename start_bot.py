"""Scipt for starting the bot"""

import logging
import os

from life_bot.bot.bot_handler import LifeBotHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    life_bot_handler = LifeBotHandler(token=os.environ["TELEGRAM_TOKEN"])
    life_bot_handler.start_bot()
