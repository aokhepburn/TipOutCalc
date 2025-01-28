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
barback_tipout = 0.15
employees = {
    "Alice": {
        "role": "bartender",
        "tips earned": 120,
        "hourly wage": 10,
        "hours worked": 5,
        "total": 0,
    },
    "Iris": {
        "role": "bartender",
        "tips earned": 120,
        "hourly wage": 10,
        "hours worked": 8,
        "total": 0,
    },
    "James": {
        "role": "server",
        "tips earned": 80,
        "hourly wage": 5,
        "hours worked": 10,
        "total": 0,
    },
    "Sasha": {
        "role": "barback",
        "tips earned": 0,
        "hourly wage": 15,
        "hours worked": 2,
        "total": 0,
    },
}
shift_totals = {
    "bartender pool": {
        "bartender total tips": 0,
        "bartender total hours": 0,
        "bartender tipout": 0,
        "bartender hourly": 0,
    },
    "server pool": {
        "server total tips": 0,
        "server total hours": 0,
        "server tipout": 0,
        "server hourly": 0,
    },
    "barback pool": {
        "barback total tips": 0,
        "barback total hours": 0,
        "barback hourly": 0,
    },
}


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


# Working on calculating barback tips. Have to add tipout to server & bartender roles FIRST which will allow barbacks information to be created/worked on. I figure I can use the below as a helper function to clean up the collect_shift_information function.
# IN calculating_hourly ONLY if bb_hours > 0 will (bt_tips - bt tipout / bt_hours) else (bt_tips/bt_hours) and there won't be tipout money going to nowhere
# COLLECT_SHIFT_INORMATION CURRENTLY DOES NOT CALCULATE HOURLY
# Could do this a few different ways. Could also not do this till I calculate hourly, ie run calculate hourly for bartenders with a if barback hours > 0 run tipout calc there??
def calculating_tipout():
    shift_totals["bartender pool"]["bartender tipout"] = (
        shift_totals["bartender pool"]["bartender total tips"] * barback_tipout
    )
    shift_totals["server pool"]["server tipout"] = (
        shift_totals["server pool"]["server total tips"] * barback_tipout
    )
    shift_totals["barback pool"]["barback total tips"] = (
        shift_totals["bartender pool"]["bartender tipout"]
        + shift_totals["server pool"]["server tipout"]
    )


def collect_shift_information():
    # for loop to collect information from the employees list for the entire shift. the entire shift represented by the dict shift_totals
    # this currently only collects barback information for hours as their money relies on the tips of the bartenders and servers
    for employee in employees:
        #!access to the totals! dict: shift_totals["role pool"] hashable: shift_totals["role pool"]["role totals"]
        if employees[employee]["role"] == "bartender":
            shift_totals["bartender pool"]["bartender total tips"] += employees[
                employee
            ]["tips earned"]
            shift_totals["bartender pool"]["bartender total hours"] += employees[
                employee
            ]["hours worked"]

        if employees[employee]["role"] == "server":
            shift_totals["server pool"]["server total tips"] += employees[employee][
                "tips earned"
            ]
            shift_totals["server pool"]["server total hours"] += employees[employee][
                "hours worked"
            ]
        if employees[employee]["role"] == "barback":
            shift_totals["barback pool"]["barback total hours"] += employees[employee][
                "hours worked"
            ]

        calculating_tipout()


def calculating_tipped_hourly():

    if shift_totals["barback pool"]["barback total hours"] > 0:
        # NEED TO ADD AND IF TOTAL HOURS FOR INDIVIDUAL ROLES ARE TRUE SO WE NEVER END UP DIVIDING BY 0 ACCIDENTALLY
        if shift_totals["bartender pool"]["bartender total hours"] > 0:
            shift_totals["bartender pool"]["bartender hourly"] += (
                shift_totals["bartender pool"]["bartender total tips"]
                - shift_totals["bartender pool"]["bartender tipout"]
            ) / shift_totals["bartender pool"]["bartender total hours"]
        if shift_totals["server pool"]["server total hours"] > 0:
            shift_totals["server pool"]["server hourly"] += (
                shift_totals["server pool"]["server total tips"]
                - shift_totals["server pool"]["server tipout"]
            ) / shift_totals["server pool"]["server total hours"]
        shift_totals["barback pool"]["barback hourly"] += (
            shift_totals["barback pool"]["barback total tips"]
            / shift_totals["server pool"]["server total hours"]
        )

    else:
        if shift_totals["bartender pool"]["bartender total hours"] > 0:
            shift_totals["bartender pool"]["bartender hourly"] = (
                shift_totals["bartender pool"]["bartender total tips"]
                / shift_totals["bartender pool"]["bartender total hours"]
            )
        if shift_totals["server pool"]["server total hours"] > 0:
            shift_totals["server pool"]["server hourly"] = (
                shift_totals["server pool"]["server total tips"]
                / shift_totals["server pool"]["server total hours"]
            )
        shift_totals["barback pool"]["barback hourly"] = 0


def employee_tipout():
    # for loop over employees to calculate total wages for the night
    for employee in employees:
        if employees[employee]["role"] == "bartender":
            employees[employee]["total"] += (
                shift_totals["bartender pool"]["bartender hourly"]
                * employees[employee]["hours worked"]
            ) + (
                employees[employee]["hourly wage"] * employees[employee]["hours worked"]
            )
        if employees[employee]["role"] == "server":
            employees[employee]["total"] = (
                shift_totals["server pool"]["server hourly"]
                * employees[employee]["hours worked"]
            ) + (
                employees[employee]["hourly wage"] * employees[employee]["hours worked"]
            )
        if employees[employee]["role"] == "barback":
            employees[employee]["total"] += (
                shift_totals["barback pool"]["barback hourly"]
                * employees[employee]["hours worked"]
            ) + (
                employees[employee]["hourly wage"] * employees[employee]["hours worked"]
            )


# add_new_employee()

collect_shift_information()
calculating_tipped_hourly()
employee_tipout()
print(shift_totals)
print(employees)
print(shift_totals)
exit()
"""extend programme to ask if there is another worker"""


"""“`
try:
age = int(input(“How old are you? “))
print(“You were born in”, 2021 – age)
except ValueError:
print(“That doesn’t look like a valid age.”)
“`"""
