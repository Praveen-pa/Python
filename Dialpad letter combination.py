a={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
c=a.copy()
f=c.keys()
b=input("Enter a number :")
if(len(b)==1):
    for i in f:
        if(i==int(b)):
            print(c[i])
else:
    e=b[0]
    d=b[1]
    m=[ ]
    for i in f:
        if(i==int(e)):
            for j in f:
                if(j==int(d)):
                    g=c[i]
                    h=c[j]
                    for k in g:
                        for l in h:
                            n=k+l
                            m.append(n)
                    print("LIST :",m)
