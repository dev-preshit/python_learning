#Exercise 9
# Python program to convert text to speech explanation
# Write a program to pronounce list of names using win32 API. 

"""
	This program uses the Windows Speech API (SAPI) to convert text to speech. 
The win32com.client module provides access to COM (Component Object Model) 
technologies, including SAPI for voice synthesis. 

1. We first create a 'speaker' object by initializing 'SAPI.SpVoice' with 
   win32com's Dispatch method, allowing us to use SAPI's Speak method.
2. A list of names ('names') is defined with values like "ram", "sham", "dham", 
   and "amman".
3. A loop iterates over each name in the list, constructs a phrase for each name 
   (e.g., "Shoutout to ram"), and then uses 'speaker.Speak(s)' to convert 
   the text into speech.
4. A delay of 1 second between each pronunciation is set using time.sleep(1) 
   to make each name more distinguishable.

This setup requires the `pywin32` library to be installed, as it provides 
the necessary components to interface with Windows-specific APIs.
"""

import win32com.client as mas
import time

speaker = mas.Dispatch("SAPI.SpVoice") 

names = ["ram","sham","dham","amman"]

for name in names:  
	s = f"Shoutout to {name}" 
	speaker.Speak(s)
	time.sleep(1)