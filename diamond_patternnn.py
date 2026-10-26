n=int(input())
for i in range(n):
        row=" "*(n-i-1)+"/"+"  "*i+'\\'
        print(row)
        
for j in range(n):
    row=" "*(j)+"\\"+"  "*(n-j-1)+'/'
    print(row)
    
