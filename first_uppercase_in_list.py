def get_first_upper_letter(string):
    # complete this function
    ls=[]
    res=''
    for j in string:
        ls.append(j)
    for i in range(len(ls)):
        if ls[i].isupper():
            res=ls[i]
            break
    return res


string = input()
upper_case_character = get_first_upper_letter(string)
print(upper_case_character)
