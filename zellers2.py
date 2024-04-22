def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def zellers_formula(k, m, D):
    if k < 0 or m < 0:
        return "Invalid input: Negative values are not allowed."
    if D < 1900 or D > 9999:
        return "Year does not exist."

    if m < 3:
        m += 12
        D -= 1

    D = D % 100
    C = D // 100

    # Adjustments for leap years
    if m in [3, 4]:
        D -= 1
    if is_leap_year(D + 1900):
        D -= 1

    # Zeller's Congruence formula
    f = (k + (13 * (m + 1) // 5) + D + (D // 4) + (C // 4) - (2 * C)) % 7

    return f

# Example usage
k = int(input("Enter k value: "))
m = int(input("Enter m value: "))
D = int(input("Enter D value: "))

day_of_week = zellers_formula(k, m, D)

if isinstance(day_of_week, int):
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(f"The day of the week for {k}/{m}/{D} is: {days_of_week[day_of_week]}")
else:
    print(day_of_week)
