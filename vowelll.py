a=input()
res =""
for i in range(0,len(a)):
    if a[i] in "aeiouAEIOU":
        continue
    else:
        res=res+a[i]
print(res)
