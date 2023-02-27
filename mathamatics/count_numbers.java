class count_numbers
{
    public static void main(String[] args)
    {
        int num=54646;
        int count=0;
        while (num != 0){
            num = num/10;
            count++;
        }
        System.out.printf("count of nums:"+	count);
    }
}