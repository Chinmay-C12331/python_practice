a=input()
a=a.replace(" ","")
a=a.replace("'","")
a=a.lower()
if a==a[::-1]:
    print(True)
else:
    print(False)
