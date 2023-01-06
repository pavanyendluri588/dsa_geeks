class tailing_zeros_of_a_factorial
{
     int no_of_tailing_zeros_of_a_factorial(int num)
        {
            int nos=0;
            for(int i=5;i<num;i=i*5)
               {
                    nos=nos+(num/i);
               }
            return nos;
        }
     public static void main(String[] args)
        {
              tailing_zeros_of_a_factorial obj =new tailing_zeros_of_a_factorial();
              System.out.printf("result:"+obj.no_of_tailing_zeros_of_a_factorial(251));
        }
}