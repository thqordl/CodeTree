import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
                     
        int ab = 60*a + b;
        int cd = 60*c + d;

        System.out.print(cd-ab);
    }
}