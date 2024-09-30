principal = 0
rate = 0
time = 0

while principal <= 0 :
    principal = float(input("Enter your principal amount: "))
    if principal <= 0 :
        print("Principal amount can't be less than or equal to Zero")
        
while rate <= 0 :
    rate = float(input("Enter your interest rate: "))
    if rate <= 0 :
        print("Interest rate amount can't be less than or equal to Zero")
        
while time <= 0 :
    time = int(input("Enter your time in year: "))
    if time <= 0 :
        print("Time can't be less than or equal to Zero")
        
total = round(principal * pow((1 + rate/100), time), 2)

print(f"Balance afer {time} year/s is: BDT {total}")