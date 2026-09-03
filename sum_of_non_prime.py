n=int(input())
sum=0
for i in range(1,n+1):
    s=int(input())
    fac=0
    for j in range(2,s):
        if s%j==0:
            fac+=1
    if fac!=0:
        sum+=s
print(sum)
