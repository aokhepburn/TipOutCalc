from TotalTips import TotalTips
from Employee import Employee

totalShiftTips: TotalTips = TotalTips(int(input("Enter the shifts total tips:")))

employee1: Employee = Employee(
    (input("Enter Employee name ")),
    int(input("Enter hours worked ")),
    input("Enter role "),
)
employee2: Employee = Employee(
    (input("Enter Employee name ")),
    int(input("Enter hours worked ")),
    input("Enter role "),
)
employee3: Employee = Employee(
    (input("Enter Employee name ")),
    int(input("Enter hours worked ")),
    input("Enter role "),
)

totalHours = employee1.hours + employee2.hours + employee3.hours

if employee1.role == employee2.role:
    if employee3.role == employee2.role:
        hourly = totalShiftTips.totalTips / totalHours
    else:
        print("Employee roles are not matched")

print(
    f"{employee1.name} is paid {employee1.hours * hourly} \n {employee2.name} is paid {employee2.hours * hourly} \n {employee3.name} is paid {employee3.hours * hourly}"
)
