number = int(input("Enter a Number: "))
value = 0
for i in range(number):
    for j in range(i):
        value = value +1
        print(value,end=" ")
    print()