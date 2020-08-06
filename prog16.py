number = int(input("Ente a number: "))
val = 0
for i in range(2,number):
    if number%i==0:
        val =1

if (val==0 and number!=1):
    print("Prime_number")

else:
    print("Not prime")

