c = input("nhap: ")
c = c.split()
print(c)
m = c[0]
p =''
m1 = ''
dem = 1
for i in range(1,len(c)):
    m = m +' '+ str(c[i])
    
    
for  i in range(len(m)-1):
    if m[i] == m[i+1]:
        dem += 1
    else:
        if dem == 1:
            l = ""
        else:
            l = str(dem)
        m1 = m1+str(l)+m[i+1]
        dem = 1
print(m1) 
        
        