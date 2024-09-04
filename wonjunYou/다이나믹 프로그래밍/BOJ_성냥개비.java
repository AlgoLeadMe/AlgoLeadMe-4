import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static final int MAX_RANGE = 100;
    static long[] dp;
    static int[] numbers = {1, 7, 4, 2, 0, 8};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        dp = new long[MAX_RANGE + 1];
        Arrays.fill(dp, Long.MAX_VALUE);

        init();
        calculateMinNumber();

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());

            StringBuilder sb = new StringBuilder();
            sb.append(dp[n]).append(" ");

            int count;

            if (n % 2 == 0) {
                count = n / 2;
            } else{
                sb.append("7");
                count = (n - 3) / 2;
            }

            sb.append("1".repeat(count));

            System.out.println(sb);
        }
    }

    private static void calculateMinNumber() {
        for (int i = 9; i < 101; i++) {
            for (int j = 2; j <= 7; j++) {
                Long number = dp[i - j] + String.valueOf(numbers[j - 2]);
                dp[i] = Math.min(Long.parseLong(number), dp[i]);
            }
        }
    }

    private static void init() {
        dp[2] = 1;
        dp[3] = 7;
        dp[4] = 4;
        dp[5] = 2;
        dp[6] = 6;
        dp[7] = 8;
        dp[8] = 10;
    }

}
