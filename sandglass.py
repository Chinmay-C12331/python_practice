n=int(input())
t=0
k=0
for i in range(1,n):
    t=n-i+1
    if t==1:
        break
    if i==1:
        row="* "*n
    else:
        row=" "*(i-1)+"* "*t
    print(row)

for i in range(1,n+1):
    k=n-i
    if i==1:
        row=" "*(n-1)+"* "
    elif i==n:
        row="* "*n
    else:
        row=" "*k+"* "*i
    print(row)
