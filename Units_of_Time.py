days = int(input("Input the number of days."))
hours = int(input("Input the number of hours."))
minutes = int(input("Input the number of minutes."))
seconds = int(input("Input the number of seconds."))

time = str(days * 86400 + hours * 3600 + minutes * 60 + seconds)
print("There are " + time + " seconds in the time inputted.")