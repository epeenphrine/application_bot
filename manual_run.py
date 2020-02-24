from app_bot import AppBot
import time 


bot = AppBot()
def run():
    bot.login()
    time.sleep(4)
    bot.find_jobs()
    bot.filter_jobs()

def apply():
    bot.manual_apply()

