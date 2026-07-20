d=input()
n=int(input())
if d=="Sunday":
    day=0
elif d=="Monday":
    day=1
elif d=="Tuesday":
    day=2
elif d=="Wednesday":
    day=3
elif d=="Thursday":
    day=4
elif d=="Friday":
    day=5
else:
    day=6
    
t=(day+n-1)%7
if t==0:
    print("Sunday")
elif t==1:
    print("Monday")
elif t==2:
    print("Tuesday")
elif t==3:
    print("Wednesday")
elif t==4:
    print("Thursday")
elif t==5:
    print("Friday")
else:
    print("Saturday")
