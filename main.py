q = [['S','P',0],['R',0],['S','M',0],['S','P',0],['S','T',0],['S','P',0],['S','C',0],['S','M',0]]
o = []
a = []
b = ""
i=0
while len(q)>0:
    if q[0][0]=='S':
        b=q[0][1]
        o.append(q[0])
        if (b=='C' or b=='T') and q[0][2]<2:
            a=q.pop(0)
            a1 = a.pop(2)
            a1+=1
            a.append(a1)
            q.append(a)
        else:       
            q.pop(0)   
    else:
        if b=='C' or b=='T':
            o.append(q[0])
            q.pop(0)
        else:
            a=q.pop(0)
            a1 = a.pop(1)
            a1 +=1
            a.append(a1)
            q.append(a)
print(o)