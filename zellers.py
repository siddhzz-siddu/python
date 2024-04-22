k=int(input("enter k value:"))
m=int(input("enter m value:"))
D=int(input("enter D value:"))
def zellers_formula(k,m,D):
    if m < 3:
        m += 12
        D -= 1
    
    D = D % 100
    C= D// 100
    
    # Zeller's Congruence formula
    f= (k + (13 * (m + 1) // 5) + D +(D//4) +(C// 4)- (2 * C)) % 7
    
    return f
# Example usage
'''k = 1
m = 9
D = 2024'''
day_of_week = zellers_formula(k,m,D)
days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f"The day of the week for {k}/{m}/{D} is: {days_of_week[day_of_week]}")