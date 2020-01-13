from datetime import date, time, datetime

#get date and time
today = datetime.now()
#get today's date
date = today.strftime("%Y:%m:%d")
#get time
time = today.strftime("%H:%M:%S")

print("Current date and time : ", date, time)
