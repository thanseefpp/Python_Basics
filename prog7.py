number = int (input("Enter a number to show multiplication table:\n"))

size = int (input("how many: "))
for x in range(1,size):
    print(number, "X" , x , "=" , number*x)
