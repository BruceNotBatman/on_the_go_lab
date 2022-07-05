a,b = int(input("Enter a number: ")), int(input("Enter another number: "))

if ((a%b)==0) or ((b%a)==0):
    print("divisible")
else:
    print("not divisible")

a,b = int(input("Enter a number: ")), int(input("Enter another number: "))

if b!=0:
    print(a/b)

a,b,c =str(input("Enter a name: ")), str(input("Enter a name: ")), str(input("Enter a name: "))

if a.lower() == b.lower() ==c.lower(): 
    print("Equal")
