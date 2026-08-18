n=int(input())
sum=(n*4)-5
for i in range(1,n+1):
    if i==1:
        row="*  "+" "*sum+"*"
    elif i==n:
        row="* "*(n*2-1)+"*"
    else:
        lrs=" "*(2*(i-2))
        sum-=4
        row="* "+lrs+"* "+" "*sum+" * "+lrs+"*"
    print(row)
        
