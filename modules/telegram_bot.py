import requests
from config import TG_API_TOKEN, CHAT_ID

class TelegramBot:

    def __init__(self, data_to_send):
        self.url = f"https://api.telegram.org/bot{TG_API_TOKEN}/"
        self.data_to_send = data_to_send

        self.send_all_data_to_bot()


    def send_all_data_to_bot(self):
        # If received data is list
        if isinstance(self.data_to_send, list):
            for data in self.data_to_send:
                # Create post captions
                caption = (
                    f"🛒 *{data['product_name']}*\n"
                    f"💰 {data['price']}\n"
                    f"🏷️ {data['discount']}\n"
                    f"Old price: {data['old_price']}\n"
                    f"From: {data['website']}\n"
                    f"🔗 [Go to product]({data['url']})"
                )

                params = {
                    "chat_id": CHAT_ID,
                    "photo": data["image"],
                    "caption": caption,
                    "parse_mode": "Markdown"
                }

                response = requests.get(self.url + "sendPhoto", params=params)

        else:
            # Send error message
            params = {
                "chat_id": CHAT_ID,
                "text": self.data_to_send,
                "parse_mode": "Markdown"
            }

            response = requests.get(self.url + "sendMessage", params=params)
