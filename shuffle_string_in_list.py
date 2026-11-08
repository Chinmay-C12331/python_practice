def shuffle_string(string, indexes_list):
    # complete this function\
    ls=[]
    res=''
    for _ in string:
        ls.append(_)
    for j in indices_list:
        i=int(j)
        res+=ls[i]
    return res
        
        


string = input()
indices_list = input().split()

result = shuffle_string(string, indices_list)
print(result)
