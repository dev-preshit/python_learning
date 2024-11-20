from plyer import notification
import time
import os


def reminder():
    notification.notify(
        title="This is a notification",
        message="Drink water",
        timeout=15 # Duration in seconds
    )


def is_enabled():
    # Check the toggle file
    if os.path.exists("D:/git/osmodule/switch.txt"):
        with open("D:/git/osmodule/switch.txt", "r") as file:
            toggle = file.read().strip().upper()
            return toggle == "ON"
    return False     

while True:
    if is_enabled():
        hour = time.strftime('%H')
        wait = int(hour)
        if wait % 2 == 0:
            reminder()
        time.sleep(3600)  # Wait for 1 hour
    else:
        time.sleep(10)
