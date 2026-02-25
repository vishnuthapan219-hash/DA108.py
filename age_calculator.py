# age calculator 
print ("Enter your birth details\n")
day = int(input("Day: "))
month = int(input("Month: "))   
year = int(input("Year: "))
from datetime import date
today = date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print ("Your age is: ", age)        
print ("Days lived: ", (today - date(year, month, day)).days)
