#Execise 9
# Python program to convert text to speech...
# Write a program to pronounce list of names using win32 API. 

import win32com.client as mas
import time

speaker = mas.Dispatch("SAPI.SpVoice") 

names = ["ram","sham","dham","amman"]

for name in names:  
	s = f"Shoutout to {name}" 
	speaker.Speak(s)
	time.sleep(1)