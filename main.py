"""
Main point
"""

from modules.all_parser import AllParser
from modules.telegram_bot import TelegramBot

if __name__ == "__main__":
    parser_result = AllParser()
    tg_bot = TelegramBot(parser_result.data_to_send)