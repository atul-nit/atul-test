from datetime import date

# today = date.today()
# print(type(today))
# print("today's date is",today)

# Get day, month and year separately
today = date.today()
# print("day",today.day,"month",today.month,"year",today.year)
# #
print("today's weekday",today.weekday())

"""Task: print weekday name instead of value"""
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# week_number = today.weekday()
# print("today is {}".format(weekdays[week_number]))



# d1 = date(2019,5,10)
# print(d1)
# d2 = date.today()
# print(d2)
# d3 = d2 - d1
# print(d2-d1)
# print(d3.days)


from datetime import datetime

# def diff_month(d1, d2):
#     return (d1.year - d2.year) * 12 + d1.month - d2.month

# print(diff_month(datetime(2010,10,1), datetime(2010,9,14)))
# print(diff_month(datetime(2010,10,1), datetime(2009,10,1)))
# assert diff_month(datetime(2010,10,1), datetime(2009,11,1)) == 11
# assert diff_month(datetime(2010,10,1), datetime(2009,8,1)) == 14

