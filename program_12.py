num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))

if(num1>num2 or num2>num3):
    if(num1>num3):
        print(num1, "is greatest")
    elif(num2>num3):
        print(num2, "is greatest")    
else:
    print(num3, "is greatest")
