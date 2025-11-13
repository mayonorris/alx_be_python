#Personal Daily Reminder :Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.


# Prompt for a single task (loop until non-empty)
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Please enter a non-empty task.\n")

# Prompt for priority (high/medium/low), loop for validation
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in {"high", "medium", "low"}:
        break
    print("Please enter 'high', 'medium', or 'low'.\n")

# Prompt for time sensitivity (yes/no), loop for validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in {"yes", "no"}:
        break
    print("Please answer 'yes' or 'no'.\n")

# Build the base message using match/case
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        # Shouldn't happen due to validation, but just in case:
        print("Unknown priority.")
        exit(1)

# Modify message based on time sensitivity
if time_bound == "yes":
    print(f"\nReminder: {base} that requires immediate attention today!")
else:
    if priority == "high":
        print(f"\nReminder: {base}. Aim to schedule it today if possible.")
    elif priority == "medium":
        print(f"\nNote: {base}. Try to slot it into your plan.")
    else:  # low
        print(f"\nNote: {base}. Consider completing it when you have free time.")

