import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
import pytz
import threading
import time
from plyer import notification

# Replace with your own OpenWeatherMap API key
API_KEY = "your_openweathermap_api_key"
CITY = "London"
COUNTRY = "GB"

def get_uk_time():
    tz = pytz.timezone("Europe/London")
    return datetime.now(tz).strftime("%H:%M:%S")

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def get_uk_temperature():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        temp = data['main']['temp']
        return f"{temp}°C"
    except:
        return "Error"

def update_info():
    uk_time_label.config(text=f"UK Time: {get_uk_time()}")
    uk_temp_label.config(text=f"UK Temp: {get_uk_temperature()}")
    sys_time_label.config(text=f"System Time: {get_current_time()}")
    root.after(10000, update_info)  # Update every 10 seconds

def start_timer():
    try:
        seconds = int(timer_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
        return

    def countdown():
        for i in range(seconds, -1, -1):
            timer_label.config(text=f"Timer: {i} sec")
            time.sleep(1)
        show_notification()

    threading.Thread(target=countdown, daemon=True).start()

def show_notification():
    notification.notify(
        title='Timer Done!',
        message='Your timer has finished.',
        timeout=5
    )

# GUI setup
root = tk.Tk()
root.title("UK Time, Temp, Timer & Notification")
root.geometry("400x300")

uk_time_label = tk.Label(root, text="UK Time:", font=("Helvetica", 14))
uk_time_label.pack(pady=10)

uk_temp_label = tk.Label(root, text="UK Temp:", font=("Helvetica", 14))
uk_temp_label.pack(pady=10)

sys_time_label = tk.Label(root, text="System Time:", font=("Helvetica", 14))
sys_time_label.pack(pady=10)

timer_entry = tk.Entry(root, font=("Helvetica", 12))
timer_entry.pack(pady=5)
timer_entry.insert(0, "Enter timer in seconds")

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

timer_label = tk.Label(root, text="Timer: 0 sec", font=("Helvetica", 14))
timer_label.pack(pady=10)

update_info()
root.mainloop()