"""Scipt for starting the bot"""

import logging
import os

from life_bot.bot.bot import LifeBotBuilder

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    life_bot_builder = LifeBotBuilder(token=os.environ["TELEGRAM_TOKEN"])
    life_bot_builder.start_bot()
