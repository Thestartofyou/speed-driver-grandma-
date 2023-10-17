from gtts import gTTS
import os
import time

# Set the speed limit (in km/h)
speed_limit = 60

def check_speed(speed):
    if speed > speed_limit:
        exceed_speed = speed - speed_limit
        message = f"You are exceeding the speed limit by {exceed_speed} kilometers per hour. Please slow down."
        tts = gTTS(text=message, lang='en')
        tts.save("speed_warning.mp3")
        os.system("mpg123 speed_warning.mp3")

# Simulate speed changes (replace this with a real speed source)
current_speed = 50  # Initial speed in km/h
while True:
    check_speed(current_speed)
    time.sleep(5)  # Simulate a speed check every 5 seconds
    current_speed += 5  # Simulate a speed increase (replace with real speed data)
