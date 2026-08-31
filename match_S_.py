a=input()
b=input()
t=""
if len(a)==len(b):
    for i in range(0,len(a)):
        if i%2!=0:
            t+=b[i]
        else:
           t+=a[i]
    print(t)
