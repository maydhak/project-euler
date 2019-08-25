"""
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Logic: determine whether or not the year is leap. We only care about the first of the month, so add the number
# of days for that month. Check if that day is a Sunday (taking Sunday as the 7th day of the week, then just
# check if days_sum % 7 == 0) and if so, add 1 to the sum. Repeat for all years in the 20th century.

months_and_days = {
    "jan": 31, "feb": 28, "mar": 31, "apr": 30, "may": 31, "jun": 30,
    "jul": 31, "aug": 31, "sep": 30, "oct": 31, "nov": 30, "dec": 31,
}


def leap_year(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    months_and_days['feb'] = 29 if leap else 28
    return months_and_days['feb']


def solution19():
    num_of_sundays = 0
    year = 1900
    days_sum = 1

    for year in range(year, 2001):
        leap_year(year)
        for month in months_and_days:
            days_sum += months_and_days[month]
            if year == 1900:  # the problem only cares about 1 Jan 1901 onwards
                pass
            elif days_sum % 7 == 0:
                num_of_sundays += 1
        year += 1

    return num_of_sundays


print(solution19())

# In hindsight, because dicts are unordered, was it just luck that Python correctly iterated over the dictionary each
# time? Because really, the order in which the number of days in the month are added to the sum affects whether or not
# the program correctly determines if the day of the week is a Sunday.
