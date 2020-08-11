# input from user
# input() function only takes string value from users,
# if you need to do any mathematical operations then you might
# need to convert the string to int or float
user_input=input("Enter a positive imteger in second")
time=int(user_input)
day_unit=24*3600
hour_unit=3600
min_unit=60
if time<60:
    print("0 days 0 hours 0 minutes", time, "seconds")
elif 60<=time<3600:
    minutes=time//60
    time=time%60
    print("0 days 0 hours", minutes, "minutes", time, "seconds")
elif 3600<=time<day_unit:
    hours=time//hour_unit
    time=time%hour_unit
    minutes=time//min_unit
    time=time%min_unit
    print("0 days", hours, "hours", minutes, "minutes", time, "seconds")
else:
    days=time//day_unit
    time=time%day_unit
    hours=time//hour_unit
    time=time%hour_unit
    minutes=time//min_unit
    time=time%min_unit
    seconds=time
    print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
