n=int(input())
print("* "*n)
for i in range(0,n-1):
    i=n-i-1
    print("+ "*i)
    

for j in range(1,n+1):
    print("* "*j)
for k in range(0,n):
    k=n-k
    print("* "*k)
