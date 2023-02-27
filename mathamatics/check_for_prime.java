class check_for_prime
{
     static String check_num_is_prime(int num)
        {
           int c=0;
           if (num==1)
               {
                   return "False";      
               }
           for(int i=2;i<num;i++)
               {
                  if (num/i==0)
                      {
                           c=1;
                           break;
                      }
               }
           if (c==1){
               return "False";
           }else{
     
               return "True";}
     
        }
     static String check_num_is_prime_eff1(int num)
          {
            if(num==1)
               {
                    return "False";
               }
            for (int i=1;i*i<num;i++)
                 {
                     if(num/i==0)
                         {
                            return "False";
                         }
                 }
            return "True";

          }
     public static void main(String[] args)
       {
          System.out.printf("result:"+check_num_is_prime(5));
          System.out.println("\neff1:result:"+check_num_is_prime_eff1(5));
       }
}