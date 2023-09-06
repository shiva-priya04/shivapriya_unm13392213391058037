#factorial using recursive
n=int(input("enter a no.:"))
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
print(fact(n))