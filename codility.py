from datetime import datetime

def remaining_balance(A, D):
    balances = {}
    cp = {}
    total_cf = 0

    for amount, date in zip (A, D):
        date = datetime.strptime(date, '%Y-%m-%d')
        yr, mth =  date.year, date.month

        if yr != 2020:
            continue

        if mth not in balances:
            balances[mth] = 0
        balances[mth] += amount

        if amount < 0:
            if mth not in cp:
                cp[mth] = []

            cp[mth].append(amount)

    for mth in range(1, 13):
        if mth not in cp or len(cp[mth]) < 3 or sum(cp[mth]) > -100:
            balances[mth] = balances.get(mth, 0) - 5
            total_cf += 5

    return sum(balances.values())

print(remaining_balance([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))  # Expected output: 230
print(remaining_balance([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))  # Expected output: 25
print(remaining_balance([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))  # Expected output: -164
print(remaining_balance([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))  # Expected output: 80
print(remaining_balance([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))  # Expected output: -115