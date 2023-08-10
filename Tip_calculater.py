print ("Welcome to tip Calculater......")
bill = float(input ("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15?"))
slipt_bill = int(input("How many people to slipt the bill? "))
percentage = (tip/bill)*100
total_bill = bill+percentage
pay = total_bill/slipt_bill
print(f"Each person should pay: {round(pay, 2)}")
