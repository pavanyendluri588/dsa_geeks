class palinbdrome_number
{
    String palindrome_number_check(int num)
    {
        int orginal=num;
        int palin=0;
        int last=0;
        while (num!=0)
           {
               last=num-((num/10)*10);
               palin=palin*10+last;
               num=num/10;
           }
        System.out.print("orginal:"+orginal+"\npalin:"+palin+"\n");
        if (palin==orginal)
            {
               return "Yes";
            }
        else
            {
               return "No";
            }
    }
    public static void main(String[] args)
      {
         
                palinbdrome_number obj =new  palinbdrome_number();     
                System.out.printf("result:"+obj. palindrome_number_check(566765));     

      }
}