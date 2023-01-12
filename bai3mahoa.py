a = open('bai3.inp','r')
b = open('bai3.out','w')
k = a.readline().split()
n = int(k[0])
hv =k[1]
c = a.readline()
t = ''
c2 = []
d = 0
mangc = ''
phu1 =''
phu = ''
e = ''
if len(c) % n != 0:
    p = ' ' * (n - len(c) % n)
    c += p
for i in range(len(c)):
    t = t+c[i]
    d+=1
    if d == n:
        c2 = c2 + [t]
        t = ''
        d = 0
for i in range(int(len(c)/n)):
    phu = c2[i]
    for j in range(len(hv)):
        phu1 = phu1 + phu[int(hv[j])-1]
    mangc = mangc + phu1
    phu1 = ''
for i in range(int(len(c)/n)):
    if c2[i] in mangc:
        if not c2[i] in e: 
            e = e + c2[i]+' '
b.writelines(str(mangc + '\n'))
b.writelines(str(e))
a.close()
b.close()
    
        
        
    