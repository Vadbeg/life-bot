from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


class LifeBotBuilder(ApplicationBuilder):
    def __init__(self, token: str):
        super().__init__()

        self.token(token=token)
        self._application: Application = self.build()

        self._application.add_handler(CommandHandler("start", start))

    def start_bot(self):
        self._application.run_polling()
