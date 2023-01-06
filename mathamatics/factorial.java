class factorial
{
    int factorial_number(int num)
       {
          int c=1;
          while(num>1)
           {
                c=c*num;
                num=num-1;
           } 
    
          return c;
       }
    public static void main(String[] args)
       {
        factorial obj = new factorial();
        System.out.printf("result:"+obj.factorial_number(5));   
       }
}