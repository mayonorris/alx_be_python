"""
Learning Objectives:
- Use the datetime module to get/format current date & time
- Perform date arithmetic with timedelta
"""

from datetime import datetime, date, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Prompts for days, computes future date, and prints it."""
    while True:
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Please enter a valid integer.\n")

    today = date.today()
    future_date = today + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return (future_date)

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
