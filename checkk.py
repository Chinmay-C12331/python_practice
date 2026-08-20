a=input()
if a.isdecimal():
    print("Digit")
elif a.islower():
    print("Lowercase Letter")
elif a.isupper():
    print("Uppercase Letter")
else:
    print("Special Character")
