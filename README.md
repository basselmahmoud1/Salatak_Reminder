# 🕌 Prayer Reminder App

A simple Python application that fetches **daily Salah (prayer) times** based on your city and reminds you before each prayer — with terminal notifications and Adhan sound.

---

## 📦 Features

- ✅ Fetches prayer times using [Aladhan API](https://aladhan.com/prayer-times-api)
- ✅ Supports **any country and city**
- ✅ Displays prayer times in a clean, 12-hour format with emoji-enhanced layout
- ✅ Reminds you **10 minutes before prayer**
- ✅ Plays Adhan sound at exact prayer time
- ✅ Automatically updates next day’s timings at midnight
- ✅ Can be converted into a Windows `.exe` app

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/prayer-reminder-app.git
cd prayer-reminder-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> You’ll need:
> - `requests` for fetching data
> - `pygame` for playing Adhan sound

### 3. Add Adhan Sound

Place your `adan.mp3` file in the same folder as the code.

---

## ▶️ Run the App

```bash
python main.py
```

You’ll be prompted to enter your country and city. The app will run in the terminal and notify you before each prayer.

---

## 🪄 Optional: Build as Executable (.exe)

To convert this app into a standalone Windows `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```

Then run the `.exe` inside the `dist` folder.

---

## 💡 Example Cities

- Egypt → Cairo, Alexandria
- Saudi Arabia → Mecca, Riyadh
- USA → New York, Chicago
- UK → London, Birmingham
- Turkey → Istanbul, Ankara

---

## 🙏 Author

Made with ❤️ by Bassel Mahmoud  
[LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).