from app_bot import AppBot
import time
bot = AppBot()
bot.login()
time.sleep(4)
bot.click_job()
bot.iframe_handler()
bot.question_handler()