import java.util.Scanner;

public class Main {
    public static int day(int m, int d) {
        int[] month = new int[]{0,31,29,31,30,31,30,31,31,30,31,30,31};
        int day = 0;

        for(int i=0; i<m; i++) {
            day += month[i];
        }
        day += d;
        return day;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        String A = sc.next();
        
        int dif = day(m2,d2) - day(m1,d1);
        int cnt = dif/7;
        int week = dif%7;

        if(A.equals("Mon")) {System.out.print(cnt+1);}
        else if(A.equals("Tue") && week>=1) {System.out.print(cnt+1);}
        else if(A.equals("Wed") && week>=2) {System.out.print(cnt+1);}
        else if(A.equals("Thu") && week>=3) {System.out.print(cnt+1);}
        else if(A.equals("Fri") && week>=4) {System.out.print(cnt+1);}
        else if(A.equals("Sat") && week>=5) {System.out.print(cnt+1);}
        else if(A.equals("Sun") && week==6) {System.out.print(cnt+1);}
        else System.out.print(cnt);
    }
}