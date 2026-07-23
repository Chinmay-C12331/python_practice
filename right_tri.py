n=int(input())
num=-1
for i in range(0,n):
    i=n-i
    num+=1
    print((("  ")*num)+("* ")*i)
