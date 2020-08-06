list = []

number = int(input("Enter array size: "))

count =0

for i in range(0,number):
    elements = int(input())

    list.append(elements)

print("Entered Array values: ",list)

for x in list:
    if x % 2==0:
        count = count+1

print("Number of even numbers : ",count)