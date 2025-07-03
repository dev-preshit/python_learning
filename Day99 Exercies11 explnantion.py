#Exercise 11
"""
This program uses the plyer module to show desktop notifications and
relies on a text-based toggle switch to control whether the reminders should be active.

    The reminder() function uses plyer.notification.notify() to display a
    desktop notification with a title and a message ("Drink water") for 15 seconds.

    The is_enabled() function checks the status of a toggle switch stored in a
    file named switch.txt located at D:/git/osmodule/.

        If the file exists and contains the text "ON" (case-insensitive), it
        returns True; otherwise, it returns False.

        This acts as a control mechanism to turn the reminder system on or off
        without closing the program.

    Inside the infinite while True loop:

        The program continuously checks if the toggle is enabled using is_enabled().

        If enabled:

            It retrieves the current hour using time.strftime('%H'), converts it to an integer, and checks if it's an even hour (wait % 2 == 0).

            If the condition is met, it calls the reminder() function to show the notification.

            After that, it waits for 1 hour (3600 seconds) before checking again.

        If the toggle is not enabled, it waits just 10 seconds before checking again.

This setup requires the plyer module to be installed for cross-platform notification support.
It's a simple and customizable reminder system that runs in the background and responds to a local file-based switch.
"""

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
