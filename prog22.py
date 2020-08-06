
size = int(input("Ente the size of 2D array:"))
array1 = []
array2 = []
sum = []
def getArray(size):
    array=[]
    for i in range(size):
        col =[]
        for j in range(size):
            val=int(input())
            col.append(val)
        array.append(col)
        print()
    return array

def sumArray(size,array1,array2):

    for i in range(size):
        col =[]
        for j in range(size):
            val =array1[i][j]+array2[i][j]
            col.append(val)
        sum.append(col)
    return sum

def displayArray(size,sum):
    '''print("Array_1 :")
    for i in range(size):
        for j in range(size):
            print(array1[i][j],end=" ")
        print()
    print("Array_2: ")
    for i in range(size):
        for j in range(size):
            print(array2[i][j],end=" ")
        print()'''

    #print("Sum of array:")
    for i in range(size):
        for j in range(size):
            print(sum[i][j],end=" ")
        print()

print("Enter values to First Array: ")
array1=getArray(size)
print("Enter values to Second Array: ")
array2=getArray(size)
sumArray(size,array1,array2)
print("Sum of Array :")
displayArray(size,sum)



