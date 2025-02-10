function roundNum(x) {
    (Math.round(x * 100) / 100).toFixed(2)
    return x
}
let srvAsstTipout = 5
let employees = {
    "alice": {
        "role": "bartender",
        "tipsEarned": 120,
        "hourlyWage": 10,
        "hoursWorked": 5,
        "total": 0,
    },
    "iris": {
        "role": "bartender",
        "tipsEarned": 120,
        "hourlyWage": 10,
        "hoursWorked": 8,
        "total": 0,
    },
    "james": {
        "role": "server",
        "tipsEarned": 80,
        "hourlyWage": 5,
        "hoursWorked": 10,
        "total": 0,
    },
    "sasha": {
        "role": "svrAsst",
        "tipsEarned": 0,
        "hourlyWage": 15,
        "hoursWorked": 2,
        "total": 0,
    }
}
let shiftTotals = {
    "bartenderPool": {
        "bartenderTotalTips": 190,
        "bartenderTotalHours": 0,
        "bartenderTipOut": 0,
        "bartenderHourly": 0,
    },
    "serverPool": {
        "serverTotalTips": 100,
        "serverTotalHours": 0,
        "serverTipOut": 0,
        "serverHourly": 0,
    },
    "svrAsstPool": {
        "svrAsstTotalTips": 0,
        "svrAsstTotalHours": 0,
        "svrAsstHourly": 0,
    },
}

function setSvrAsstTipout() {/*to add when HTML is set up */ }

function addNewEmployee() {/*to add when HTML is set up */ }
//check
// for loop that collects the information from the dict "employees" and adds information to "shiftTotals"
function collectShiftInformation() {
    for (let key of Object.keys(employees)) {
        if (employees[key].role == "bartender") {
            shiftTotals.bartenderPool.bartenderTotalHours += employees[key].hoursWorked
            shiftTotals.bartenderPool.bartenderTotalTips += employees[key].tipsEarned
        }
        else if (employees[key].role == "server") {
            shiftTotals.serverPool.serverTotalHours += employees[key].hoursWorked
            shiftTotals.serverPool.serverTotalTips += employees[key].tipsEarned
        }
        else if (employees[key].role == "svrAsst") {
            shiftTotals.svrAsstPool.svrAsstTotalHours += employees[key].hoursWorked
        } else { console.log("role not recognized") }
    }
    return shiftTotals
}
// check
// adds the tips for svrAssts by taking percentages of total tips
function calculatingTipOut() {

    shiftTotals.bartenderPool.bartenderTipOut = roundNum(
        (shiftTotals.bartenderPool.bartenderTotalTips * srvAsstTipout));
    shiftTotals.serverPool.serverTipOut = roundNum(
        (shiftTotals.serverPool.serverTotalTips * srvAsstTipout));
    shiftTotals.svrAsstPool.svrAsstTotalTips = roundNum(
        shiftTotals.bartenderPool.bartenderTipOut
        + shiftTotals.serverPool.serverTipOut)
    console.log(shiftTotals)
    return shiftTotals
}
function calculatingTippedHourly() {
    if (shiftTotals.svrAsstPool.svrAsstTotalHours > 0) {
        let btHourly = (
            shiftTotals.bartenderPool.bartenderTotalTips
            - shiftTotals.bartenderPool.bartenderTipOut
        )
            / shiftTotals.bartenderPool.bartenderTotalHours
        shiftTotals.bartenderPool.bartenderHourly = roundNum(
            btHourly
        )
        shiftTotals.serverPool.serverTotalHours = roundNum(shiftTotals.serverPool.serverTotalTipOut
            - shiftTotals.serverPool.serverTipOut
            / shiftTotals.serverPool.serverTotalHours)

    }

    return shiftTotals
}
/*if shift_totals["svrasst pool"]["svrasst total hours"] > 0:
 
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
shift_totals["svrasst pool"]["svrasst hourly"] = 0*/

function employeeTipOut() { }

calculatingTipOut()
collectShiftInformation()
calculatingTippedHourly()
console.log(shiftTotals)

