x=int(input())
n=int(input())

sum=0
p=1
s=1 
for i in range(n):
    sum+=s*(x**p)
    p+=2
    s*=-1
print(sum)
