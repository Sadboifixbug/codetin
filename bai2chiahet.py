3a = open('chiahet.inp','r')
b = open('chiahet.out','a+')
n = a.readline()
e = 0
i = e
t = 1
dem = 0
d = 0
while e == 0:
    i += 1
    if i % t ==0:
        d +=1
        if  d == t:
            t +=1
            d = 0
        dem += 1
    if dem == int(n):
        b.writelines(str(i))
        e = 1
a.close()
b.close()