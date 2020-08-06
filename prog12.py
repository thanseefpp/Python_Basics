Array = []
size = int (input("Enter Size of Array: "))

print("Enter values to Array: ")

for i in range(0,size):
    arrayValues = int(input())

    Array.append(arrayValues)
print("Before Sort :",Array)

Array.sort(reverse =True)
print("After Sort: ",Array)



