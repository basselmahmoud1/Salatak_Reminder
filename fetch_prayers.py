import requests
from datetime import datetime


def get_prayer (country, city ) :
    Raw_data = requests.get(f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=5")
    data_req = Raw_data.json() # return the dictionary
    day_miladi = data_req["data"]['date']["readable"]
    day_hejri = data_req["data"]['date']["hijri"]['date']
    prayer_times = data_req["data"]['timings']
    # rearrange the salawat
    sala_order = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
    ordered_prayers = { sala : prayer_times[sala] for sala in sala_order}
    # Make the time in 12-hr formate
    ordered_prayers_times_str = {}
    ordered_prayers_times_int = {}
    for sala , time in ordered_prayers.items() :
        time_obj = datetime.strptime(time, "%H:%M")
        time_12hr = time_obj.strftime("%I:%M %p")
        # Convert the str to real time
        ordered_prayers_times_str[sala] = time_12hr
        ordered_prayers_times_int[sala] = (time_obj.hour,time_obj.minute)
    return {
        "miladi_date": day_miladi,
        "hijri_date": day_hejri,
        "prayer_times_str": ordered_prayers_times_str,
        "prayer_times_int": ordered_prayers_times_int
    }
#times = get_prayer(city= "Cairo")
# print (times["miladi_date"])
# print (times["hijri_date"])
# print (times["prayer_times_str"])
#print(times["prayer_times_int"])



