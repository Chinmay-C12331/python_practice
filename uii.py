a=int(input())
b=input()
if b.isdecimal():
  if a==int(b):
    print("Successfully matched!!!")
  else:
    print("NO Match!!")
elif a.isalnum():
  print("Enter only digit as string")
else:
  print("Enter number as string")
