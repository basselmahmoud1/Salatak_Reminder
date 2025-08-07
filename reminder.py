import datetime
import time
from fetch_prayers import get_prayer
import os
import contextlib
with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
    import pygame


def play_adhan():
    pygame.mixer.init()
    pygame.mixer.music.load("adan.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # wait for the music to finish
        continue

def reminder(pray_data):
    now = datetime.datetime.now()
    prayer_times = pray_data["prayer_times_int"]
    sala_order = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]

    next_prayer = None
    for sala in sala_order:

        hour , minute = prayer_times[sala]
        prayer_time = datetime.datetime(now.year, now.month, now.day, hour, minute)
        if prayer_time > now:
            next_prayer= (sala,prayer_time)
            break
    if not next_prayer:
        fajr_hour, fajr_min = prayer_times["Fajr"]
        next_day = now + datetime.timedelta(days=1)
        prayer_time = datetime.datetime(next_day.year, next_day.month, next_day.day, fajr_hour, fajr_min)
        next_prayer = ("Fajr", prayer_time)
    sala_name, sala_time = next_prayer

    delta = sala_time - now
    hours_left = delta.seconds // 3600
    minutes_left = (delta.seconds % 3600) // 60

    print(f"\n{'✨ NEXT PRAYER ✨':^45}")
    print(f"➡️  {sala_name.upper():<10} at ⏰ {pray_data['prayer_times_str'][sala_name]} 🕌")
    print(f"⏳ Time remaining: {hours_left:02d}h {minutes_left:02d}m 🕒\n")

    while True:
        now = datetime.datetime.now()
        delta = sala_time - now
        minutes_left = int(delta.total_seconds() // 60)
        #print(minutes_left)
        if minutes_left == 10:
            print(f"🔔 10 minutes left until {sala_name} prayer!")
            time.sleep(30)

        if minutes_left <= 0:
            print(f"🕌 It's time for {sala_name} prayer!")
            try:
                play_adhan()  #
                break
            except:
                print("Adhan alarm could not be played. (Make sure the file exists or use another method.)")
            break
        time.sleep(30)


