import math
a = int(input('nhap'))
kq  = True
def snt(k):
    kq = True
    for i in range(2,int(math.sqrt(k))+1):
        if k % i == 0:
            kq = False
            break
    print(kq)        
if a == 1 or a == 2:
    print('True')
else:
    snt(a)