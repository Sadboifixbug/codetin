import math
dem = 0
a = open('soprime.inp','r')
e = a.readline()
e = int(e)
a.close()
b = open('soprime.out','a+')
def kt(n):
    kq = True
    if n == 3:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    else:
        for i in range(2,round(math.sqrt(n))+1):
            if n % i == 0:
                kq = False
                return kq
                break
            else:
                return True
        
        
for k in range(1,10000):
    if kt(k) == True:
        dem += 1
    if dem == e:
        b.writelines(str(k))
        break
b.close()
