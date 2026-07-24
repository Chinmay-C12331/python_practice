n=int(input())
num=-1
j=0
for i in range(0,n):
    i=n-i
    num+=1
    #print(num)
    if i==n:
        j=(n*2)-1
        print((((" ")*num)+("* ")*j))
    else:
        gap=(num*2)-2
        print((" "*num)+("* "*i)+(" "*gap)+("* "*(i)))
