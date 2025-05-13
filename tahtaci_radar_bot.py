
import requests
import datetime
import telegram
import os

# Get environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=BOT_TOKEN)

def fetch_dummy_data():
    # Placeholder logic, replace with real scraping/analysis
    return {
        'hisse': 'TERA',
        'rsi': '38 ➡ 52',
        'hacim': '3 gün üst üste artıyor',
        'yorum': 'Fiyat sabit, hacim yükseliyor. Tahtacı yükleniyor olabilir!'
    }

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    signal = fetch_dummy_data()
    message = f"""
🚨 TESPİT: Olası MAL TOPLAMA
📌 Hisse: {signal['hisse']}
📊 RSI: {signal['rsi']}
📈 Hacim: {signal['hacim']}
💬 Yorumu: {signal['yorum']}
🕓 Zaman: {now}
    """
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == '__main__':
    main()
