def is_leap(year):
    leap_year = False
    
    # Write your logic here
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    return leap_year

year = int(input())
print(is_leap(year))
