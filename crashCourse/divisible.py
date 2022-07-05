a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if ((a%b)==0):
    print("divisible")
elif((b%a)==0):
    print("divisible")
else:
    print("not divisible")