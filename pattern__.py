n=int(input())
t=0
for i in range(1,n+1):
    if i==1:
        row="* "*((n*2)-1)
        print(row)
    else:
        t=n-i
        row="  "*((i*2)-2)+"* "*((t*2)+1)
        print(row)
