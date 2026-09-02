n=int(input())
for i in range(0,n+2):
    row=""
    for s in range(i):
        row+=" "
    for j in range(1,n-i+1):
        row+=str(j)+" "
    print(row)
