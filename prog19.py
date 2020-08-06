income = int(input("Enter your annual income: "))

if income>250000 and income<=500000:
    Tax =(income*5)/100
    print("You have to pay tax :",Tax)
elif income>500000 and income<=1000000:
    Tax =(income*20)/100
    print("You have to pay tax :",Tax)
elif income>1000000 and income<=5000000:
    Tax= (income*30)/100
    print("You have to pay tax :",Tax)
elif income>5000000:
    print("Income tax officers will visit your home :) ")

else:
    print("Not Tax")