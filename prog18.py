writtenScore = int(input("Enter Written test score: "))
labScore = int(input("Enter Lab test score: "))
assignments = int(input("Enter Assignment score: "))

Total_Grade = ((writtenScore*70)/100)+((labScore*20)/100)+((assignments*10)/100)
print("Your Total grade is :",Total_Grade)