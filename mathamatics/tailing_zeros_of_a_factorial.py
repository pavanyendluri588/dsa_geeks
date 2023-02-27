def tailing_zeros(n):
    c=0
    a=5
    for i in range(5,n+1,):
        c=c+(n/a)
        a=a*5
        if a>n:
            break
    return int(c)
x=int(input("Enter number:"))
print(tailing_zeros(251))
print("No of tailing zeros for{}:{}".format(x,tailing_zeros(x)))