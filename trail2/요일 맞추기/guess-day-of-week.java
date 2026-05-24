import java.util.Scanner;
public class Main {
    public static int day(int m, int d) {
        int[] month = new int[]{0,31,28,31,30,31,30,31,31,30,31,30,31};
        int day = 0;

        for(int i=0; i<m; i++) {
            day += month[i];
        }
        day+=d;
        return day;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();

        String[] week = new String[]{"Mon","Tue","Wed","Thu","Fri","Sat","Sun"};
        int start = day(m1, d1);
        int end = day(m2, d2);

        int weekday = ((end-start)%7+7)%7;
        System.out.print(week[weekday]);
    }
}