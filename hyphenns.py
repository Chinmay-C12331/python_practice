w=input()
res=""
for i in range(len(w)):
    if i==len(w)-1:
        res=res+w[i]
    else:
        res=res+w[i]+"-"
       
print(res)
    
