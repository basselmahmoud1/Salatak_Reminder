import time
from fetch_prayers import get_prayer
from reminder import reminder
from datetime import datetime


def print_dates(pray_data):
    print(f"{'='*45}")
    print(f"{'🕌  DAILY PRAYER TIMES':^45}")
    print(f"{'='*45}")
    print(f"📅 Miladi Date:         {pray_data['miladi_date']}")
    print(f"🗓️ Hijri Date:          {pray_data['hijri_date']}")
    print(f"{'-'*45}")
    print(f"{'🙏 Prayer':<16} {'🕒 Time':>20}")
    print(f"{'-'*45}")
    emoji_map = {
        "Fajr": "🌅",
        "Sunrise": "☀️",
        "Dhuhr": "🏙️",
        "Asr": "🌇",
        "Maghrib": "🌆",
        "Isha": "🌃"
    }
    for prayer, time in pray_data['prayer_times_str'].items():
        emoji = emoji_map.get(prayer, "")
        print(f"{emoji} {prayer:<18} {time:>20}")
    print(f"{'='*45}")

print("🌍 Prayer Time Finder 🌙")
country = input("🔹 Enter your Country: ").strip()
city = input("🏙️  Enter your City: ").strip()


print("🕌 Welcome to the Prayer Reminder App!")
print("📿 This application will remind you before every prayer.")
print("⏳ Running... Press Ctrl+C to stop.\n")
pray_data = get_prayer(country,city)
today_date = datetime.now().date()
print_dates(pray_data)

while True:
    try:
        reminder(pray_data)
        current_date = datetime.now().date()
        if current_date != today_date:
            pray_data = get_prayer(country,city)
            today_date = current_date
            print_dates(pray_data)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(60)