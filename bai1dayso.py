a = open('dayso.inp','r')
b = open('dayso.out','a+')
n = a.readline().split()
p = int(n[0])
j = int(n[1])
for i in range(4):
    kq = p**j
    kqp = str(kq)
    if len(kqp)<2:
        kqp = '0'+kqp
        p = kq
    else:
        e = kqp[len(kqp)-2]+kqp[len(kqp)-1]
        kqp = e
        p = int(kqp)
    b.writelines(kqp+' ')
a.close()
b.close()
 