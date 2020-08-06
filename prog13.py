palindrome = input("Enter a name : ")

if palindrome == palindrome[::-1]:
    print("Your entered name is Palindrome")
else:
    print("Not Palindrome")