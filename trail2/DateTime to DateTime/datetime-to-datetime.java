import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        
        int start = 0;
        int end = 0;

        start = 24*60*11 + 60*11 + 11;
        end = 24*60*a + 60*b + c;

        if(end-start<0){
            System.out.print(-1);
        } else {
            System.out.print(end-start);
        }
    }
}