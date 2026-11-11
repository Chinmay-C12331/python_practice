n=int(input())
ls=[]
for _ in range(n):
    store=input().split()
    for i in store:
        ls.append(i)
s_ls=sorted(ls)
print(s_ls)
