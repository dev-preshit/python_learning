#EXECRISE 2 EXPLANATION
#GREETING PROGRAM
#WAP in python capable of grteating with correct phase according to time

"""
    on line 8 we have imported a module called time which have 
    function of itself help with time manipulation...

    On line 13 we are using time.strftime('%H) which give 
    current local time in Hour only we can also use %M %S etc 
    i.e. 
        %H => Hours
        %M => Minutes
        %S => Seconds
        %d => Day
        %m => Months
        %Y => Years
    
    On line 24 we Typecast it to int as the time functon 
    will give string as output...
    
    After that from line 29 onwards we use simple logic of 
    if,elif,else to check various condition and print according to it...
"""
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