"""Module with bot builder"""

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


class LifeBotHandler:
    def __init__(self, token: str):
        super().__init__()

        self._application_builder = ApplicationBuilder()

        self._application_builder.token(token=token)
        self._application: Application = self._application_builder.build()

        self._application.add_handler(CommandHandler("start", start))

    def start_bot(self) -> None:
        self._application.run_polling()
