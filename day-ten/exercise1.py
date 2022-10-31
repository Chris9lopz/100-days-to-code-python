# Instructions

# You are then going to create a function called days_in_month()
# which will take a year and a month as inputs, e.g.
# And it will use this information to work out the number of days in the month, 
# then return that as the output

def is_leap(year): # leap function will determinate if is leap or not
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year):
        if month == 2:
            return 29
    else:
        return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







