num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))

if(num1<num2 and num1<num3):
    print(num1, "is smallest")
elif(num2<num1 and num2<num3):
    print(num2, "is smallest")
else:
    print(num3, "is smallest")