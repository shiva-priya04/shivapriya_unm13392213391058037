#factorial using recursive
n=int(input("enter a no.:"))
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
print(fact(n))

#leaf year
a=int(input("enter a year:"))
if a%4==0:
  print("Yes it is a leap year")
else:
  print("Not a leap year")