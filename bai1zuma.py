a = open('banbi.inp','r')
b = open('banbi.out','a+')
d = a.readline()
day = []
for i in range(len(d)):
    day = day + [d[i]]
p = a.readline().split()
k = int(p[0])
dan = p[1]
if (dan == day[k]) and (dan == day[k+1]):
    for i in range(k,len(d)):
        if dan == day[i]:
            del d[i:1]
    print(day)
    