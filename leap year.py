n=float(input("enter the value:"))
if(n>0 and n.is_integer()):
    if(n%4==0 or n%400==0):
        print('it is a leap year')
    else:
        print("it is not a leap year")
else:
    print("not a valid input")
