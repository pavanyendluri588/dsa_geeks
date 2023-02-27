def check_for_prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=1
            break
    if count==1:
         return False
    else:
         return True
def checking_for_prime_eff1(n):
    squrt=0
    count=0
    for i in range(2,n):
        if i*i>n:
            break
        if n%i==0:
           count=1
           break
    if count==1:
          return False
    else:
          return True        
x=int(input("Enter number:"))
print("checking {} is prime or not:{}".format(x,check_for_prime(x)))
print("eff1 :checking {} is prime or not:{}".format(x,checking_for_prime_eff1(x)))