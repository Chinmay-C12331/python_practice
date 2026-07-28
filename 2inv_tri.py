n=int(input())
num=-1
j=0
for i in range(0,n):
    i=n-i
    num+=1
    if i==n:
        j=(n*2)-1
        print((((" ")*num)+("* ")*j))
        #here we can reduce the value of i insted of using gap
    else:
        gap=(num*2)-2
        print((" "*num)+("* "*i)+(" "*gap)+("* "*(i)))
