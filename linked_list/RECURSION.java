
public class RECURSION
{
    public static void main(String[] args) {
        int count=0;
        int num =500;
        System.out.println( count_digit(num,count));
    }
    
    public static int count_digit(int num,int count){
    if (num>0){
        count=count+1;
        num=num/10;
        return count_digit(num,count);
    }
    else{
        return count;
    }
}
    
    
    
    
    
}
