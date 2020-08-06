num = int(input("Choose a day: "))

switcher = {
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    7:"Saturday",
}
x = switcher.get(num)
if x == None:
    print("INVALID !")
else:
    print(x)
