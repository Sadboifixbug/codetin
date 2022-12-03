import array as arr
m2 =[]
a = open('square.inp','r')
k = a.readline().split()
y = int(k[0])
x = int(k[1])
print(y,' ',x)
for i in range (y):
    m = a.readline().split()
    m2.insert(i,m)
