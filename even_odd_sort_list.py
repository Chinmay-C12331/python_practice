n=input().split()
num=[]
ls_odd=[]
ls_even=[]
for _ in n:
    num.append(int(_))
for i in range(len(num)):
    if num[i]%2==0:
        ls_even.append(num[i])
    else:
        ls_odd.append(num[i])
ls_even.sort()
ls_odd.sort()
print(ls_even)
print(ls_odd)
        
