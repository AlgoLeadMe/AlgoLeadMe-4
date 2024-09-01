import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String[] data = reader.readLine().split(" ");
        int N = Integer.parseInt(data[0]);
        int M = Integer.parseInt(data[1]);

        int[] scores = new int[N + 1];

        data = reader.readLine().split(" ");
        for (int i = 1; i <= N; i++) {
            scores[i] = Integer.parseInt(data[i - 1]);
        }

        // 세 번째 줄 입력 처리
        data = reader.readLine().split(" ");
        int A = Integer.parseInt(data[0]);
        int D = Integer.parseInt(data[1]);

        reader.close();

        int upper = (N + D - 1) / D; // 최대 헌혈 가능 횟수

        int[][] dp = new int[upper + 1][N + D];

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= upper; j++) {
                if (j != 0 && dp[j][i - 1] == 0) continue;

                dp[j][i] = Math.max(dp[j][i], dp[j][i - 1] + scores[i]);

                if (j != upper) {
                    dp[j + 1][i + D - 1] = Math.max(dp[j + 1][i + D - 1], dp[j][i - 1] + A);
                }
            }
        }

        for (int i = 0; i <= upper; i++) {
            int maxScore = 0;

            for (int j = 0; j < dp[i].length; j++) {
                maxScore = Math.max(maxScore, dp[i][j]);
            }

            if (maxScore >= M) {
                System.out.println(i);
                return;
            }

        }

        System.out.println(-1);
    }

}
