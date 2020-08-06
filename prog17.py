
number1 = int(input("Enter two numbers: \n"))
number2 = int(input())

choice = int(input("Choose a option\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))

class Calculator():
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2

    def addition(self):
        sum=self.number1+self.number2
        print("Addition_Result:",sum)
    def subtract(self):
        sum=self.number1-self.number2
        print("Subtract_Result:",sum)
    def multiply(self):
        sum=self.number1*self.number2
        print("Multiply_Result:",sum)
    def division(self):
        sum=self.number1/self.number2
        print("Division_Result:",sum)

obj =Calculator(number1,number2)

if choice==1:
    sum=obj.addition()
    
elif choice==2:
    sum=obj.subtract()
    
elif choice==3:
    sum=obj.multiply()
    
elif choice==4:
    sum=obj.division()
    
else:
    print("Wrong choice")