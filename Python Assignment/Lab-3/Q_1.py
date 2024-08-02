# Write a function called check-season. It takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    month = month.lower()
    if month == 'january' or month == 'jan' or month == 'february' or month == 'feb'or month == 'december' or month == 'dec':
        return 'Winter'
    elif month == 'march' or month == 'mar' or month == 'april' or month == 'apr' or month == 'may':
        return 'Spring'
    elif month == 'june' or month == 'july' or month == 'august' or month == 'aug':
        return 'Summer'
    elif month == 'september' or month == 'sep' or month == 'october' or month == 'oct' or month == 'november' or month == 'nov':
        return 'Autumn'
    else:
        return 'Enter the month Correctly'

month = input("Enter the month: ")
print(check_season(month))
