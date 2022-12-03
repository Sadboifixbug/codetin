a = open('tongle.inp','r')
n = a.readline()
m = a.readline().split()
a.close()
t = 0
for  i in range(int(n)):
    if int(m[i]) % 2 !=0:
        t += int(m[i])
a = open('tongle.out','w+')
a.writelines(str(t))
a.close()