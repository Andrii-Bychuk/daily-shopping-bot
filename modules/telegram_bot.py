import requests
from config import TG_API_TOKEN, CHAT_ID

class TelegramBot:

    def __init__(self, data_to_send):
        self.url = f"https://api.telegram.org/bot{TG_API_TOKEN}/sendPhoto"
        self.data_to_send = data_to_send

        self.send_all_data_to_bot()


    def send_all_data_to_bot(self):
        for data in self.data_to_send:
            # Create post captions
            caption = {
                f"🛒 *{data["product_name"]}*\n"
                f"💰 {data["price"]}\n"
                f"🔗 [Go to product]({data["url"]})"
            }

            params = {
                "chat_id": CHAT_ID,
                "photo": data["image"],
                "caption": caption,
                "parse_mode": "Markdown"
            }

            response = requests.get(self.url, params=params)
