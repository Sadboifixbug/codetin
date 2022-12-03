#2.xauconchung
a = open('bai2.inp','r')
b = open('bai2.out','a+')
a_1 = a.readline()
a_2 = a.readline()
a1 = ''.join(a_1)
a2 = ''.join(a_2)
kq = 0
dem = 1
d = 0
print(a1)
print(a2)
for i in range(1,len(a2)-2):
    for j in range(1,len(a1)):
        if (a1[j] == a2[i]):
            for  k in range(j,len(a1)+1):
                if d+i <= len(a2)-2:
                    if a1[k] == a2[d+i]:    
                        dem += 1
                        d +=1 
                    if dem > kq:
                        kq = dem
                    else:
                        d = 0
                        dem = 1
                        break
e = str(kq)
b.writelines(e)
a.close()
b.close()
