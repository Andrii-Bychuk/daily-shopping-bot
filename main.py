"""
Main point
"""
import json

from modules.maudau import AllParser
from modules.telegram_bot import TelegramBot

if __name__ == "__main__":
    maudau = AllParser()
    tg_bot = TelegramBot(maudau.result)