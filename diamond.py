n=int(input())
num=n
nun=0
for i in range(1,n+1):
    #print(num-1)
    num-=1
    print(((" ")*num)+(str(i)+" ")*i)
for i in range (1,n):
    i=n-i
    nun+=1
    print(((" ")*nun)+(str(i)+" ")*i)
   # print(i)
