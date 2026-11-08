def is_prime(n):
    # compete this function
    ls=[]
    for i in range(2,n+1):
        is_p= True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_p=False
                break
        if is_p:
            ls.append(str(i))
    return " ".join(ls)

n = int(input())

print(is_prime(n))
