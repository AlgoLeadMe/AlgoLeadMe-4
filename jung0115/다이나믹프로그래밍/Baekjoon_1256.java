package jung0115.다이나믹프로그래밍;
// 13차시 2024.09.23.월 : 백준 - 사전(1256)

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon_1256 {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());

    int N = Integer.parseInt(st.nextToken()); // a의 개수
    int M = Integer.parseInt(st.nextToken()); // z의 개수
    int K = Integer.parseInt(st.nextToken()); // 몇 번째 문자열을 찾아야 하는지

    StringBuilder answer = new StringBuilder();

    long[][] dp = new long[ N + M + 1 ][ N + M + 1 ];
    dp[0][0] = 1;

    for(int i = 1;i <= N + M; i++){
      dp[i][0] = 1;
      dp[i][i] = 1;
      for(int j = 1; j < i; j++){
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
      
        if(dp[i][j] > 1000000000)
          dp[i][j] = 1000000001;
      }
    }

    // 사전에 수록되어 있는 문자열의 개수가 K보다 작을 경우
    if(dp[N + M][N] < K) {
      answer.append("-1");
    }
    else {
      while (N != 0 || M != 0) {
        if(dp[N + M - 1][M] >= K) {
          answer.append("a");
          N--;
        }
        else {
          answer.append("z");
          K -= dp[N + M - 1][M];
          M--;
        }
      }
    }

    System.out.print(answer);

  }
}
