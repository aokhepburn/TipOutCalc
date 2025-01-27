"""employee enters:
name
role
tips_earned
hourly_wage
hours_worked
employee recieves:
walk_total_tips
walk_wage
walk_total

program collects
total_tips
total_hours"""

# filled in for testing only
employees = {
    "Alice": {
        "role": "bartender",
        "tips earned": 120,
        "hourly wage": 10,
        "hours worked": 5,
    },
    "James": {
        "role": "server",
        "tips earned": 80,
        "hourly wage": 5,
        "hours worked": 10,
    },
}
total_hours = 0
total_tips = 0


# def add_new_employee():
#     name = input("Employee:Name")
#     role = input("Employee:Role")
#     tips_earned = int(input("Employee:Tips Earned"))
#     hourly_wage = int(input("Employee:Hourly Wage"))
#     hours_worked = int(input("Employee:Hours Worked"))

#     """When we expand programme role will play a bigger role indicating tip out or pool. """
#     employees.update(
#         {
#             name: {
#                 "employee role": role,
#                 "tips earned": tips_earned,
#                 "hourly wage": hourly_wage,
#                 "hours worked": hours_worked,
#             }
#         }
#     )

#     add_more_employees = input("Add another employee Y/N").lower()
#     if add_more_employees == "y":
#         add_new_employee()
#     else:
#         '''next step print() will just become return and then '''
#         print(employees)


def collect_shift_information():
    global total_tips
    global total_hours
    for employee in employees:
        total_tips += int(employees[employee]["tips earned"])
        total_hours += int(employees[employee]["hours worked"])

    print(total_tips)
    print(total_hours)


def calculate_tip_hourly():
    global total_tips
    global total_hours
    hourly = total_tips / total_hours
    for employee in employees:
        hourly = hourly * employees[employee]["hours worked"]
        employees[employee].update({"walk tips": hourly})
        print(employee, employees[employee]["walk tips"])


# add_new_employee()
collect_shift_information()
calculate_tip_hourly()
exit()
"""extend programme to ask if there is another worker"""


"""“`
try:
age = int(input(“How old are you? “))
print(“You were born in”, 2021 – age)
except ValueError:
print(“That doesn’t look like a valid age.”)
“`"""
