
class Area:
    def circle(self):
        pi=3.14
        radius=int(input("Enter radius of circle: "))
        area=pi*radius**2
        print("Area of Circle: ",area)

    def square(self):
        sqr=int(input("Enter length of square :"))
        area=sqr*sqr
        print("Area if Square :",area)
    def rectangle(self):
        rec_length=int(input("Enter length of Rectangle: "))
        rec_width=int(input("Enter width of Rectangle:"))
        area=rec_length*rec_width
        print("Area of Rectangle: ",area)
    def Triangle(self):
        height=float(input("Enter the height of Triangle: "))
        base =float(input("Enter the base of Triangle:"))
        area=(base*height)/2
        print("Area of Triangle :",area)


class Myclass(Area):
    def wrong(self):
        print("Wrong choice !")

obj=Myclass()

while True:
    choice = int(input("1.Circle\n2.Square\n3.Rectangle\n4.Triangle\n5.Exit\n"))

    if choice == 1:
        area=obj.circle()

    elif choice == 2:
        area=obj.square()
    elif choice == 3:
        area=obj.rectangle()

    elif choice == 4:
        area=obj.Triangle()
    elif choice == 5:
        break
    else:
        obj.wrong()