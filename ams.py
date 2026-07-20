a=input()
n=len(a)
ams=0
for i in range(n):
    ams += int(a[i])**n
    
if ams == int(a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
