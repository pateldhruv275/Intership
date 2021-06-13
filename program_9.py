num = int(input("Enter number \n"))

if(num<100):
    print(num ,"is less than 100")
    if(num%2==0):
        print(f"{num} Number is Even")
    else:
        print(f"{num} Number is odd") 

else:
    print(num ,"is not less than 100")