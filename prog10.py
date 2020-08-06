list = []
list2 =[]
number = int(input("Enter number of elements : "))


print("Enter number to first array :")
for x in range(0,number):
    elements = int(input())
    list.append(elements)

print("Enter values to second array:")

for i in range(0,number):
    elements = int(input())
    list2.append(elements)

print("Before Swapping:")
print("First Array:\n",list)
print("Second Array :\n",list2,"\n")
temp = list
list = list2 
list2 = temp
print("After Swapping:")
print("First Array:\n",list)
print("Second Array :\n",list2)


