n=int(input())
r=""
rev=""
for i in range(1,n+1):
    r+=str(i)
    rev=str(r[::-1])
    print(r+rev[1:])
