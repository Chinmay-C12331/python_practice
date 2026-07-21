n=int(input())
count=0
num=0
t=0
while t<2:
    count=0
    num=0
    while count<n:
        num+=1
        print((str(num))*num)
        count+=1
    t+=1
