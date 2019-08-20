# from datetime import datetime

# get current date along with hours, minutes, seconds and milliseconds
# today = datetime.now()
# print(today)
#
# print(datetime.date(today))
# # get only time
# t = datetime.time(datetime.now())
# print(t)

# create a date
# x = datetime(2020, 5, 17, 11)
# print(x)
# print(x.weekday())

# use of strftime
# x = datetime(1991, 1, 14,16, 23, 33)
# x = datetime.now()
# print(x)
# print(x.strftime("%a"))
# print(x.strftime("%A"))
# print(x.strftime("%b"))
# print(x.strftime("%B"))
# print(x.strftime("%y"))
# print(x.strftime("%Y"))
# print(x.strftime("%m"))
# print(x.strftime("%-m"))
# print(x.strftime("%d"))
# print(x.strftime("%-d"))
# print(x.strftime("%x"))
# print(x.strftime("%X"))
# print(x.strftime("%U"))
# print(x.strftime("%p"))
# print(x.strftime("%H"))
# print(x.strftime("%I"))
# print(x.strftime("%j"))


# from datetime import datetime
#
# date_time_str = '2018-12-29 08:15:27.342215'
# date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
#
# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)