a = open('chiaqua.inp','r')
b = open('chiaqua.out','w+')
k = a.readline().split()
n = int(k[0])
m = int(k[1])
e = list(map(int , a.read().split()))
vt = []
d = 0
c = 0
kq = ''
if sum(e) % m != 0:
    kq ='-1'
else:
    tb = sum(e)/m
    for j in range(n):
        c += 1
        if c <= n:
            if sum(e[d:c]) >tb:
                kq = '-1'
                break
            elif sum(e[d:c]) == tb:
                vt += [str(d+1)+' '+str(c)]
                d = c 
        else:
            kq = '-1'
            break
if kq == '-1':
    b.writelines(kq)
else:
    for i in range(m):
        b.writelines(str(vt[i])+'\n')
a.close()
b.close()