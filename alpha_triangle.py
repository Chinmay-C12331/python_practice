a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input())
r=""
for i in range(1,n+1):
    r=" ".join(a[0:i])
    print(r)

# --------second approch---------

#time complexity is same O(n^2)


#for i in range(1,n+1):
#    row=""
#    for j in range(i):
#        row+=a[j]+" "
#    print(row)
