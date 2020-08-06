array1 = []
size =int(input("Enter the size of Array: "))

for i in range(0,size):
    val =int(input())
    array1.append(val)

print("Before multiply",array1)
value=0
array2=[]
for i in range(0,size-1):
    value=array1[i]*array1[i+1]
    array2.append(value)
print("Multiplied Array: ",array2)