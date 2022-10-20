a={1:['.','..'],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'],0:[' ']}
b=input("digit :")
c=a.copy()
k=c.keys()
if(len(b)==1):
    for i in k:
        if(i==int(b)):
            print(c[i])
else:
    d=b[0]
    e=b[1]
    m=[ ]
    for i in k:
        if(i==int(d)):
            for j in k:
                if(j==int(e)):
                    g=c[i]
                    h=c[j]
                    for f in g:
                        for l in h:
                            n=f+l
                            m.append(n)
                    print(m)
