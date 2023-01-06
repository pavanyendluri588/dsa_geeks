def factorial_num(n):
    c=1
    while n>1:
       c=c*n
       n=n-1
    return c
x=int(input("Enter number:"))
print("factoprial of ",x,":",factorial_num(x))