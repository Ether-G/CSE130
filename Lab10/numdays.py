# 1. Name:
#      Benjamin Black
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program prompts the user for a start date and an end date,
#      then calculates the number of days between those dates, accounting
#      for leap years and validating all inputs.
# 4. What was the hardest part? Be as specific as possible.
#      The most challenging part was implementing the
#      date validation logic, particularly ensuring the correct number of days for
#      each month while accounting for leap years.
# 5. How long did it take for you to complete the assignment?
#      It took approximately 4 hours

def is_leap_year(year):
    """
    Leap Year?
    
    A leap year is a year divisible by 4, except for years divisible by 100
    unless they are also divisible by 400.
    """
    assert isinstance(year, int), "Year must be an integer"
    assert year >= 1753, "Year must be 1753 or later"
    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(month, year):
    """
    Return the number of days in the specified month and year.
    function accounts for leap years when calculating February (:
    """
    assert isinstance(month, int), "Month must be an integer"
    assert 1 <= month <= 12, "Month must be between 1 and 12"
    assert isinstance(year, int), "Year must be an integer"
    assert year >= 1753, "Year must be 1753 or later"
    
    # Days in each month (index 0 is unused to align with calendar months)
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust Feb
    if month == 2 and is_leap_year(year):
        return 29
    
    return days[month]

def validate_date(year, month, day):
    """
    Validate that the provided date is valid.
    """
    try:
        year = int(year)
        if year < 1753:
            return False, "Error: Year must be 1753 or later."
    except ValueError:
        return False, "Error: Year must be an integer."
    try:
        month = int(month)
        if month < 1:
            return False, "Error: Month must be 1 or greater."
        if month > 12:
            return False, "Error: Month must be 12 or less."
    except ValueError:
        return False, "Error: Month must be an integer."
    try:
        day = int(day)
        if day < 1:
            return False, "Error: Day must be 1 or greater."
        max_days = days_in_month(month, year)
        if day > max_days:
            return False, f"Error: {month}/{year} has only {max_days} days."
    except ValueError:
        return False, "Error: Day must be an integer."
    
    return True, ""

def get_date_input(prompt_prefix):
    """
    Prompt the user for a valid date (year, month, day).
    returns a tuple (year, month, day)
    """
    while True:
        # Get year
        while True:
            year_input = input(f"{prompt_prefix} year: ")
            try:
                year = int(year_input)
                if year < 1753:
                    print("Error: Year must be 1753 or later.")
                    continue
                break
            except ValueError:
                print("Error: Year must be an integer.")
        
        # Get month
        while True:
            month_input = input(f"{prompt_prefix} month: ")
            try:
                month = int(month_input)
                if month < 1:
                    print("Error: Month must be 1 or greater.")
                    continue
                if month > 12:
                    print("Error: Month must be 12 or less.")
                    continue
                break
            except ValueError:
                print("Error: Month must be an integer.")
        
        # Get day
        while True:
            day_input = input(f"{prompt_prefix} day: ")
            try:
                day = int(day_input)
                if day < 1:
                    print("Error: Day must be 1 or greater.")
                    continue
                max_days = days_in_month(month, year)
                if day > max_days:
                    print(f"Error: {month}/{year} has only {max_days} days.")
                    continue
                break
            except ValueError:
                print("Error: Day must be an integer.")
        
        # we have a valid date!!!!
        return year, month, day

def date_to_days(year, month, day):
    """
    Convert a date to days since a ref point
    """
    assert isinstance(year, int), "Year must be an integer"
    assert isinstance(month, int), "Month must be an integer"
    assert isinstance(day, int), "Day must be an integer"
    assert year >= 1753, "Year must be 1753 or later"
    assert 1 <= month <= 12, "Month must be between 1 and 12"
    assert 1 <= day <= days_in_month(month, year), "Day must be valid for the given month and year"
    
    # Calc days for years
    days = year * 365
    
    # Add leap days for years before the current year
    # Only check years >= 1753
    for y in range(1753, year):
        if is_leap_year(y):
            days += 1
    
    # Add days for months in the current year
    for m in range(1, month):
        days += days_in_month(m, year)
    
    # Add days for the current month
    days += day
    
    return days

def main():
    """
    Main func
    """
    print("This program calculates the number of days between two dates.")
    
    # start date
    start_year, start_month, start_day = get_date_input("Start")
    
    # end date
    while True:
        end_year, end_month, end_day = get_date_input("End")
        
        # Calc
        start_days = date_to_days(start_year, start_month, start_day)
        end_days = date_to_days(end_year, end_month, end_day)
        
        # ensure end date is not before start date
        if end_days < start_days:
            print("Error: End date cannot be before start date.")
            continue
        
        break
    
    # calculate and display
    days_difference = end_days - start_days
    
    print(f"\nThere are {days_difference} days between {start_month}/{start_day}/{start_year} and {end_month}/{end_day}/{end_year}")

if __name__ == "__main__":
    main()