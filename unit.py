unit = float(input("Enter your units:"))

if(unit<100):
    charge =unit*0

elif(unit<300):
    charge = 100*0 + (unit-100)*2
elif(unit<500):
    charge =100*0 + 200*2 + (unit-300)*5
else:
    charge =100*0 + 200*2 + 200*5 + (unit-500)*7

print("Your cosst is Rs. ",charge)