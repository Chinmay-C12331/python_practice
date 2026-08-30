#a=[9,2,4,1,0,6,8,7]
#a.sort(key=None,reverse=False)
#s=sorted(a)
#print(s)
#print(a)
t=0
a=[9,2,4,1,0,6,8,7]
for i in range(0,len(a)):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print(a)
        
        
