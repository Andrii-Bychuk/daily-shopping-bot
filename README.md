# Product Promo Notifier 🛍️

This Python script automates the process of monitoring product promotions on the [Maudau](https://maudau.com.ua) website and sends relevant deals directly to a Telegram chat.

---

## 📌 Features

- Reads a list of products from a `.txt` file  
- Generates search URLs based on the product list  
- Parses product search results from maudau.com.ua  
- Extracts product name, price, and image  
- Sends results to a Telegram chat with:
  - Text formatting
  - Embedded product links
  - Product images

---

## 🗂️ Project Structure

```
project/
├── main.py
├── data/
│   └── products.txt          # List of products to track
├── modules/
│   ├── products.py           # File reading logic
│   ├── maudau.py             # Website parsing logic
│   └── telegram.py           # Telegram message sending logic (optional)
```

---

## ⚙️ Requirements

- Python 3.10+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a file called `config.py` in the root directory with the following content:

```python
TG_API_TOKEN = "YOUR TELEGRAM API TOKEN"
CHAT_ID = "YOUR TELEGRAM CHAT ID"
```

> ⚠️ Make sure to add `config.py` to `.gitignore` so you don’t commit it to GitHub.

---

## 📝 Usage

1. Add product names (one per line) into `data/products.txt`:

```
green tea
milk chocolate
instant coffee
```

2. Run the main script:

```bash
python main.py
```

3. If Telegram integration is enabled, you will receive messages like:

```
🛒 Green Tea Ahmad
💰 109 ₴
🔗 View Product → https://maudau.com.ua/search?text=green%20tea
```

---

## 📦 Telegram Integration (optional)

To enable Telegram notifications:

1. Create a bot via [@BotFather](https://t.me/BotFather)  
2. Get your bot token  
3. Start a chat with your bot (send any message)  
4. Use the following link to get your `chat_id`:  
   `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
5. Add the token and chat_id to your `config.py`

---

## ✅ Future Plans

- Add support for more e-commerce sites
- Enable price filtering
- Full Telegram bot interaction via `/start` or `/search` commands  

---

## 👨‍💻 Author

**by-Soulhunt (Andrii Bychuk)**  
Made in PyCharm & Python 💻🐍

---

*This is a personal learning project focused on web scraping, automation, and Telegram bot integration.*