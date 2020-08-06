n=int(input("Enter the number of lines: "))
for i in range(2,n+2):
    for j in range(1,i):
        print(j, end=" ")
    print("\n")