n=input().strip()
n=n.lower()
n=n.replace(" ","")
count_v=0
count_c=0
for i in range(len(n)):
    if n[i] in "aeiou":
        count_v+=1
        #print(n[i])
    else:
        count_c+=1
print(count_v)
print(count_c)
