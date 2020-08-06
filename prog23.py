
size = int(input("Enter a size of array: "))
array =[]

class OperationArray():
    def __init__(self,size,array):
        self.size=size 
        self.array=array

    def getArray(self):
        print("Enter values to Array: ")
        for i in range(self.size):
            col = []
            for j in range(self.size):
                val= int (input())
                col.append(val)
            self.array.append(col)

    def displayArray(self):
        print("Display_Array :")
        for i in range(self.size):
            for j in range(self.size):
                print(self.array[i][j],end=" ")
            print()

obj = OperationArray(size,array)
obj.getArray()
obj.displayArray()

