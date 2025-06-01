# daily reminder 

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += " that should be done as soon as possible."
    case "medium":
        if time_bound == "yes":
            reminder += " that needs to be addressed today."
        else:
            reminder += " that should be done soon."
    case "low":
        if time_bound == "yes":
            reminder += " that needs to be done by the deadline today."
        else:
            reminder += " that can be done when you have some time."
    case _:
        reminder = f"Reminder: '{task}' has an unrecognized priority."

print(reminder)