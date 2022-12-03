a = open('taphops.inp','r')
b = open('taphops.out','w+')
m = a.readline().split()
e = []
n = int(m[0])
k = int(m[1])
for  i in range(1,n+1):
    e.append(i)
s = ''   
v = e.index(k)
del e[v]
for i in range(k):
    if k < e[i]:
        break
    if (k - e[i]) in e:
        del e[e.index(k-e[i])]
    if len(e) < i:
        break
for  i in range(len(e)):
    s += str(e[i])+' '
b.writelines(s)
a.close()
b.close()