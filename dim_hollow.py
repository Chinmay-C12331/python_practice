n=int(input())
a=((2*n)-1)
for i in range(1,n+1):
    if i==1:
        row=" "*(2*(n-1))+(str(i))
    else:
        l_s=" "*(2*(n-i))
        m_s=" "*(2*i-3)
        row=l_s+str(i)+m_s+str(i)
    print(row)
for i in range(1,n):
    r=n-i
    if r==1:
        row=" "*(2*i)+str(r)
    else:
        l_s=" "*(2*i)
        m_s=" "*(2*r-3)
        row=l_s+str(r)+m_s+str(r)
    print(row)

    
