n=input().strip()
r=""
g=""
for i in range(len(n)):
    if n[i] == "R":
        r+=n[i]
    else:
        g+=n[i]
if len(g)>len(r):
    print(len(r))
else:
    print(len(g))
        
