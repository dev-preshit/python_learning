#EXECRISE 2
#GREETING PROGRAM
#WAP in python capable of grteating with correct phase according to time


import time

hour = time.strftime('%H')
hour = int(hour)

if hour >= 6 and hour < 12 :
    print("GOOD MORNING")

elif hour >= 12 and hour < 18 :
    print("GOOD AFTERNOON")

elif (hour >= 18 and hour < 24) or (hour >=0 and hour < 6) :
    print("GOOD EVENING")
else :
    print("Someting went wrong")
