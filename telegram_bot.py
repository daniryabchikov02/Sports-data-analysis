import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest
from send_to_chatgpt import send_to_chatgpt 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


TOKEN = 
print("Bot is starting..") 

request = HTTPXRequest(connect_timeout=10, read_timeout=10)
app = Application.builder().token(TOKEN).request(request).build()

async def send_daily_pick():
    channel_id = ''
    sample_output = await send_to_chatgpt("Requesting AI-generated sports prediction.")
    try:
        await app.bot.send_message(chat_id=channel_id, text=sample_output)
        logger.info("Daily pick posted to channel.")
    except Exception as e:
        logger.error(f"Failed to post daily pick to channel: {e}")

async def scheduled_task():
    while True:
        await send_daily_pick()
        await asyncio.sleep(60)

async def main():
    task = asyncio.create_task(scheduled_task())
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.stop()
    await task

if __name__ == "__main__":
    print("Bot is running...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

