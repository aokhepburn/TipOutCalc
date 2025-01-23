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

employees = {}
total_hours = 0
total_tips = 0

# name=input("Employee:Name")
# role=input("Employee:Role")
# tips_earned=input("Employee:Tips Earned")
# hourly_wage=input("Employee:Hourly Wage")
# hours_worked=input("Employee:Hours Worked")


def add_new_employee():
    name = input("Employee:Name")
    role = input("Employee:Role")
    tips_earned = input("Employee:Tips Earned")
    hourly_wage = input("Employee:Hourly Wage")
    hours_worked = input("Employee:Hours Worked")
    """When we expand programme role will play a bigger role indicating tip out or pool. """
    employees.update(
        {
            name: {
                "employee role": role,
                "tips earned": tips_earned,
                "hourly wage": hourly_wage,
                "hours worked": hours_worked,
            }
        }
    )

    add_more_employees = input("Add another employee Y/N").lower()
    if add_more_employees == "y":
        add_new_employee()
    else:
        '''next step print() will just become return and then '''
        print(employees)


add_new_employee()
exit()
"""extend programme to ask if there is another worker"""


"""“`
try:
age = int(input(“How old are you? “))
print(“You were born in”, 2021 – age)
except ValueError:
print(“That doesn’t look like a valid age.”)
“`"""
