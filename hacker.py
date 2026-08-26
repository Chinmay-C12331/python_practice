import textwrap

def wrap(string, max_width):
    result=""
    s=""
    for i in range(1,len(string)+1):
        r=string[len(s):max_width*i]
        if r=="":
            break
        s+=r
        result+=r+"\n"
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
