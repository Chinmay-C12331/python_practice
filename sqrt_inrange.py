a=int(input())
b=int(input())
sum=0
for i in range(a,b+1):
    if i**0.5 == int(i**0.5):
        sum+=1
print(sum)
