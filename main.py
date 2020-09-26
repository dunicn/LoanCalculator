import argparse
import math


def calculate_diff(p, n, i):
    all_payments = 0
    m = 1
    i = i / (12 * 100)

    while m <= n:
        dm = (p / n) + i * (p - ((p * (m - 1)) / n))
        dm = int(math.ceil(dm))
        print("Month {}: payment is {}".format(m, dm))
        all_payments += dm
        m += 1

    overpayment = all_payments - p
    print("Overpayment is :", int(overpayment))


def calculate_payment(p, n, i):
    i = i / (12 * 100)

    a = p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    a = int(math.ceil(a))
    print("Your monthly payment = {}!".format(a))

    overpayment = a * n - p
    print("Overpayment is :", int(overpayment))


def calculate_principal(a, n, i):
    i = i / (12 * 100)

    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    p = int(math.floor(p))
    print("Your loan principal = {}!".format(p))

    overpayment = a * n - p
    print("Overpayment is :", int(overpayment))


def calculate_period(p, a, i):
    i = i / (12 * 100)

    n = math.log((a / (a - i * p)), 1 + i)
    n = math.ceil(n)
    years, months = divmod(n, 12)
    years = int(years)
    months = int(months)
    if years == 1 and months != 0:
        print("It will take {} year and {} months to repay this loan!".format(years, months))
    elif years == 1 and months == 1:
        print("It will take {} year and {} month to repay this loan!".format(years, months))
    elif years < 1 and months != 1:
        print("It will take {} months to repay this loan!".format(months))
    elif years < 1 and months == 1:
        print("It will take {} month to repay this loan!".format(months))
    elif years > 1 and months == 0:
        print("It will take {} years to repay this loan!".format(years))
    else:
        print("It will take {} years and {} months to repay this loan!".format(years, months))

    overpayment = a * n - p
    print("Overpayment is :", int(overpayment))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--type", help="Loan type")
    parser.add_argument("--principal", help="p", type=float)
    parser.add_argument("--periods", help="n", type=float)
    parser.add_argument("--payment", help="a", type=float)
    parser.add_argument("--interest", help="i", type=float)

    args = parser.parse_args()

    if args.principal is not None and args.principal < 0 or \
            args.periods is not None and args.periods < 0 or \
            args.payment is not None and args.payment < 0 or \
            args.interest is not None and args.interest < 0 or \
            args.interest is None:
        print("Incorrect parameters")

    elif args.type == "diff":
        if args.principal is not None and args.periods is not None and args.interest is not None:
            calculate_diff(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")

    elif args.type == "annuity" and args.principal is None:
        calculate_principal(args.payment, args.periods, args.interest)
    elif args.type == "annuity" and args.payment is None:
        calculate_payment(args.principal, args.periods, args.interest)
    elif args.type == "annuity" and args.periods is None:
        calculate_period(args.principal, args.payment, args.interest)
