def gcd_2_numbers(a,b):
    if a>b:
        c=b
        e=b
    else:
        c=a
        e=a
    l1=[]
    d=1

    for i in range(1,(c//2)):

        if a%d==0 and b%d==0:
            l1.append(i)
        d=d+1
        if a%e==0 and b%e==0:
            l1.append(e)
        e=e-1
    return max(l1)
print("gcd:",gcd_2_numbers(60,90))

def gcd_numbers(a,b):
    if b==0:
