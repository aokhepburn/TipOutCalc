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
        "role": "svrasst",
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

function setSvrAsstTipout() { }
function addNewEmployee() { }

// check
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
function collectShiftInformation() { }
function calculatingTippedHourly() { }
function employeeTipOut() { }


