n=input().strip()
row=""
for i in range(len(n)):
    if i==0:
        row+=n[i].lower()
    elif n[i].isupper():
        a=n[i].lower()
        row+="_"+a
    else:
        row+=n[i]
print(row)
