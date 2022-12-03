a = open('laplich.inp','r')
b = open('laplich.out','w')
n = int(a.readline())
k=[]
for i in range(2):
    k = k+[a.readline().split()]