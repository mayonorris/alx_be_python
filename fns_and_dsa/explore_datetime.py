"""
Learning Objectives:
- Mastering the basics of datetime module in Python
- Understanding how to manipulate dates and times
- Implementing date arithmetic and formatting
"""
import datetime

def display_current_datetime():
    """Displays the current date and time."""
    
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date)

def calculate_future_date(days):
    """Calculates the date after a given number of days from today."""
    days = int(input("Enter number of days: "))
    today = datetime.date.today()
    future_date = today + datetime.timedelta(days=days)
    return (future_date)
