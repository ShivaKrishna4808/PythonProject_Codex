import calendar


WORKDAY_HOURS = 10
FRIDAY_HOURS = 11
USD_RATE_PER_HOUR = 11
DEFAULT_USD_TO_INR_RATE = 95.742


def calculate_month_amount(year, month):
    monday_count = 0
    wednesday_count = 0
    thursday_count = 0
    friday_count = 0

    _, days_in_month = calendar.monthrange(year, month)

    for day in range(1, days_in_month + 1):
        weekday = calendar.weekday(year, month, day)

        if weekday == calendar.MONDAY:
            monday_count += 1
        elif weekday == calendar.WEDNESDAY:
            wednesday_count += 1
        elif weekday == calendar.THURSDAY:
            thursday_count += 1
        elif weekday == calendar.FRIDAY:
            friday_count += 1

    regular_days = monday_count + wednesday_count + thursday_count
    regular_hours = regular_days * WORKDAY_HOURS
    friday_hours = friday_count * FRIDAY_HOURS
    total_hours = regular_hours + friday_hours
    usd_amount = total_hours * USD_RATE_PER_HOUR

    return {
        "month": calendar.month_name[month],
        "mondays": monday_count,
        "wednesdays": wednesday_count,
        "thursdays": thursday_count,
        "fridays": friday_count,
        "regular_hours": regular_hours,
        "friday_hours": friday_hours,
        "total_hours": total_hours,
        "usd_amount": usd_amount,
    }


def get_months_to_show():
    month_input = input(
        "Enter month number/name, or press Enter for all months: "
    ).strip()

    if month_input == "" or month_input.lower() == "all":
        return range(1, 13)

    if month_input.isdigit():
        month = int(month_input)
        if 1 <= month <= 12:
            return [month]

    for month in range(1, 13):
        month_name = calendar.month_name[month].lower()
        month_abbr = calendar.month_abbr[month].lower()
        user_month = month_input.lower()

        if user_month == month_name or user_month == month_abbr:
            return [month]

    raise ValueError("Please enter a valid month, like 1, January, Jan, or all.")


def main():
    year = int(input("Enter year: "))
    rate_input = input(
        f"Enter USD to INR rate, or press Enter for {DEFAULT_USD_TO_INR_RATE}: "
    ).strip()
    usd_to_inr_rate = (
        DEFAULT_USD_TO_INR_RATE if rate_input == "" else float(rate_input)
    )
    months_to_show = get_months_to_show()

    grand_total_hours = 0
    grand_total_usd = 0
    grand_total_inr = 0

    print()
    print(f"Calendar calculation for {year}")
    print(f"USD to INR rate: {usd_to_inr_rate}")
    print("-" * 82)
    print(
        f"{'Month':<10} {'Mon':>3} {'Wed':>3} {'Thu':>3} {'Fri':>3} "
        f"{'Mon+Wed+Thu hrs':>17} {'Fri hrs':>8} {'Total hrs':>10} {'USD':>10} {'INR':>12}"
    )
    print("-" * 82)

    for month in months_to_show:
        result = calculate_month_amount(year, month)
        inr_amount = result["usd_amount"] * usd_to_inr_rate
        grand_total_hours += result["total_hours"]
        grand_total_usd += result["usd_amount"]
        grand_total_inr += inr_amount

        print(
            f"{result['month']:<10} "
            f"{result['mondays']:>3} "
            f"{result['wednesdays']:>3} "
            f"{result['thursdays']:>3} "
            f"{result['fridays']:>3} "
            f"{result['regular_hours']:>17.2f} "
            f"{result['friday_hours']:>8.2f} "
            f"{result['total_hours']:>10.2f} "
            f"{result['usd_amount']:>10.2f} "
            f"{inr_amount:>12.2f}"
        )

    print("-" * 82)
    print(
        f"{'Grand total':>50} "
        f"{grand_total_hours:>10.2f} "
        f"{grand_total_usd:>10.2f} "
        f"{grand_total_inr:>12.2f}"
    )


if __name__ == "__main__":
    main()
