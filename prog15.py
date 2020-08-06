array = []

size = int(input("Ente size of array: "))

def getarray(size,array): #parameter
    for i in range(size):
        val = int(input())
        array.append(val)

def display(size,array):#parameter
        print(array)

getarray(size,array)#argument return
display(size,array)#argument return
