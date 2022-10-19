month = input("Input the month : ")
day = int(input("Input the day: "))
if month in ('january', 'february', 'march'):
	season = 'winter'
elif month in ('april', 'may', 'june'):
	season = 'summer'
elif month in ('july', 'august', 'september'):
	season = 'spring'
else:
    season = 'fall'
if (month == 'march') and (day > 19):
	season = 'Summer'
elif (month == 'june') and (day > 20):
	season = 'spring'
elif (month == 'september') and (day > 21):
	season = 'fall'
elif (month == 'december') and (day > 20):
	season = 'winter'
print("Season is",season)
