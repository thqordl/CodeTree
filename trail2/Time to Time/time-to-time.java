import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        
        int ab = 0;
        int cd = 0;
        int hour = 0;
        int min = 0;
        
        while (true) {
            if(hour==a && min==b) {
                break;
            }
            ab++;
            min++;
            if(min==60) {
                hour++;
                min=0;
            }
        }

        hour = 0;
        min = 0;
        while (true) {
            if(hour==c && min==d) {
                break;
            }
            cd++;
            min++;
            if(min==60) {
                hour++;
                min=0;
            }
        }
        System.out.print(cd-ab);
    }
}