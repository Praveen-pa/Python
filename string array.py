n=int(input("n="))
a=[]
for i in range(1,n+1):
    if(i%3==0):
        if(i%5==0):
            b="FizzBuzz"
            a.append(b)
        else:
            b="Fizz"
            a.append(b)
    elif(i%5==0):
        b="Buzz"
        a.append(b)
    else:
        a.append(i)
print(a)
