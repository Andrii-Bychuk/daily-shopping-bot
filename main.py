"""
Main point
"""
from modules.maudau import MaudauParser
from modules.telegram_bot import TelegramBot

if __name__ == "__main__":
    maudau = MaudauParser()
    tg_bot = TelegramBot(maudau.result)