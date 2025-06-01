# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
           print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that should be done as soon as possible.")
    case "medium":
        if time_bound == "yes":
             print(f"Reminder: '{task}' is a medium priority task that needs to be addressed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task that should be done soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that needs to be done by the deadline today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' has an unrecognized priority.")