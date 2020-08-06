array1 = []

number = int(input("Enter a size of Array: "))

print("Enter values to First Array: \n")
for i in range(0,number):
    col = []
    for j in range(0,number):

        elements= int(input())
        col.append(elements)

    array1.append(col)
    print()

array2 = []
print ("Enter values to Second Array: \n")

for i in range(0,number):
    col=[]
    for j in range(0,number):
        elements= int(input())
        col.append(elements)
    
    array2.append(col)
    print()

print("Before Adding Array 1:")

for i in range(number):
    for j in range(number):
        print(array1[i][j],end=" ")
    print()
print("Before Adding Array 2:")
for i in range(number):
    for j in range(number):
        print(array2[i][j],end=" ")
    print()
sum = []

for i in range(0,number):
    col = []
    for m in range(0,number):
        elements = array1[i][m]+array2[i][m]
        col.append(elements)

    sum.append(col)
print("Sum of Array :")
for i in range(number):
    for j in range(number):
            print(sum[i][j],end=" ")
    print()


#print("Sum of Array:\n",sum)
