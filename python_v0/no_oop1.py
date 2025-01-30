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
svrasst_tipout = 0
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
        "role": "svrasst",
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
    "svrasst pool": {
        "svrasst total tips": 0,
        "svrasst total hours": 0,
        "svrasst hourly": 0,
    },
}


def set_svrasst_tipout():
    global svrasst_tipout

    while True:
        try:
            svrasst_tipout = int(input("Enter a tipout for the server's assistants"))
            if 0 <= svrasst_tipout <= 99:
                svrasst_tipout = round((svrasst_tipout * 0.01), 2)
                print("server assistant tipout set")
                return svrasst_tipout
        except ValueError:
            print("Tipout must be a number from 0-99")


def add_new_employee():
    name = input("Enter employee name")
    role = input("Enter employee role")
    tips_earned = int(input("Enter tips earned"))
    hourly_wage = int(input("Enter employees agreed hourly wage"))
    hours_worked = int(input("Enter hours employee worked"))

    # Role will probably end up setting hourly wage.
    # Validation must be added!!!!
    employees.update(
        {
            name: {
                "employee role": role,
                "tips earned": tips_earned,
                "hourly wage": hourly_wage,
                "hours worked": hours_worked,
                "total": 0,
            }
        }
    )

    add_more_employees = input("Add another employee to the shift? Y/N").lower()
    if add_more_employees == "y":
        add_new_employee()
    else:
        print(employees)


# Working on calculating svrasst tips. Have to add tipout to server & bartender roles FIRST which will allow svrassts information to be created/worked on. I figure I can use the below as a helper function to clean up the collect_shift_information function.
# IN calculating_hourly ONLY if bb_hours > 0 will (bt_tips - bt tipout / bt_hours) else (bt_tips/bt_hours) and there won't be tipout money going to nowhere
# COLLECT_SHIFT_INORMATION CURRENTLY DOES NOT CALCULATE HOURLY
# Could do this a few different ways. Could also not do this till I calculate hourly, ie run calculate hourly for bartenders with a if svrasst hours > 0 run tipout calc there??
def calculating_tipout():
    global svrasst_tipout
    shift_totals["bartender pool"]["bartender tipout"] = round(
        (shift_totals["bartender pool"]["bartender total tips"] * svrasst_tipout), 2
    )
    shift_totals["server pool"]["server tipout"] = round(
        (shift_totals["server pool"]["server total tips"] * svrasst_tipout), 2
    )
    shift_totals["svrasst pool"]["svrasst total tips"] = (
        shift_totals["bartender pool"]["bartender tipout"]
        + shift_totals["server pool"]["server tipout"]
    )


def collect_shift_information():
    # for loop to collect information from the employees list for the entire shift. the entire shift represented by the dict shift_totals
    # this currently only collects svrasst information for hours as their money relies on the tips of the bartenders and servers
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
        if employees[employee]["role"] == "svrasst":
            shift_totals["svrasst pool"]["svrasst total hours"] += employees[employee][
                "hours worked"
            ]

        calculating_tipout()


def calculating_tipped_hourly():

    if shift_totals["svrasst pool"]["svrasst total hours"] > 0:
        # NEED TO ADD AND IF TOTAL HOURS FOR INDIVIDUAL ROLES ARE TRUE SO WE NEVER END UP DIVIDING BY 0 ACCIDENTALLY
        if shift_totals["bartender pool"]["bartender total hours"] > 0:
            shift_totals["bartender pool"]["bartender hourly"] += round(
                (
                    shift_totals["bartender pool"]["bartender total tips"]
                    - shift_totals["bartender pool"]["bartender tipout"]
                )
                / shift_totals["bartender pool"]["bartender total hours"],
                2,
            )
        if shift_totals["server pool"]["server total hours"] > 0:
            shift_totals["server pool"]["server hourly"] += round(
                (
                    shift_totals["server pool"]["server total tips"]
                    - shift_totals["server pool"]["server tipout"]
                )
                / shift_totals["server pool"]["server total hours"],
                2,
            )
        shift_totals["svrasst pool"]["svrasst hourly"] += round(
            (
                shift_totals["svrasst pool"]["svrasst total tips"]
                / shift_totals["server pool"]["server total hours"]
            ),
            2,
        )

    else:
        if shift_totals["bartender pool"]["bartender total hours"] > 0:
            shift_totals["bartender pool"]["bartender hourly"] = round(
                (
                    shift_totals["bartender pool"]["bartender total tips"]
                    / shift_totals["bartender pool"]["bartender total hours"]
                ),
                2,
            )
        if shift_totals["server pool"]["server total hours"] > 0:
            shift_totals["server pool"]["server hourly"] = round(
                (
                    shift_totals["server pool"]["server total tips"]
                    / shift_totals["server pool"]["server total hours"]
                ),
                2,
            )
        shift_totals["svrasst pool"]["svrasst hourly"] = 0


def employee_tipout():
    # for loop over employees to calculate total wages for the night
    for employee in employees:
        if employees[employee]["role"] == "bartender":
            employees[employee]["total"] += round(
                (
                    shift_totals["bartender pool"]["bartender hourly"]
                    * employees[employee]["hours worked"]
                )
                + (
                    employees[employee]["hourly wage"]
                    * employees[employee]["hours worked"]
                ),
                2,
            )
        if employees[employee]["role"] == "server":
            employees[employee]["total"] = round(
                (
                    shift_totals["server pool"]["server hourly"]
                    * employees[employee]["hours worked"]
                )
                + (
                    employees[employee]["hourly wage"]
                    * employees[employee]["hours worked"]
                ),
                2,
            )
        if employees[employee]["role"] == "svrasst":
            employees[employee]["total"] += round(
                (
                    shift_totals["svrasst pool"]["svrasst hourly"]
                    * employees[employee]["hours worked"]
                )
                + (
                    employees[employee]["hourly wage"]
                    * employees[employee]["hours worked"]
                ),
                2,
            )


set_svrasst_tipout()
# add_new_employee()
collect_shift_information()
calculating_tipped_hourly()
print(shift_totals)
employee_tipout()
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
