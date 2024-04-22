def zellers_formula(k, m, D):
    if k < 0 or k >=31:
        return "dat doest not exist"
    if m < 0 or m >=12:
        return "month doest not exist"
    
    if m < 3:
        m += 12
        D -= 1
    
    D = D % 100
    C = D // 100
    
  
    f = (k + (13 * (m + 1) // 5) + D + (D // 4) + (C // 4) - (2 * C)) % 7
    
    return f

# Example usage
k = int(input("Enter k value: "))
m = int(input("Enter m value: "))
D = int(input("Enter D value: "))

day_of_week = zellers_formula(k, m, D)

if isinstance(day_of_week, str):
    print(day_of_week)
else:
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(f"The day of the week for {k}/{m}/{D} is: {days_of_week[day_of_week]}")