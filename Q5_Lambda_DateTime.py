#Question - 5
#import datetime
#assign today using datetime object
#create lambda functions to extract year,month and day
import datetime

today=datetime.datetime.now()

year=lambda y:y.year
month=lambda m:m.month
day=lambda d:d.day

print("Year:",year(today))
print("Month:",month(today))
print("Day:",day(today))