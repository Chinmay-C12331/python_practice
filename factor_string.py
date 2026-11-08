def factors_of_n(number):
    # complete this function
    res=''
    for i in range(1,number+1):
        if number%i==0:
           res+=str(i)+" "
    return res

number = int(input())
result = factors_of_n(number)
print(result)
