// 12차시 2024.09.07.토 : 백준 - 개근상(1563)
import java.io.BufferedReader
import java.io.InputStreamReader


fun main() {
  // ✅ Input
  val br = BufferedReader(InputStreamReader(System.`in`))

  val N = br.readLine().toInt()

  // ✅ Solve
  // 출석 일수, 지각 일수, 연속 결석 일수
  val dp = Array(N + 1, {Array(2, {Array(3, {0})})})

  dp[1][0][0] = 1
  dp[1][1][0] = 1
  dp[1][0][1] = 1

  for(i: Int in 2..N) {
    dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % 1000000;
    dp[i][0][1] = dp[i-1][0][0] % 1000000;
    dp[i][0][2] = dp[i-1][0][1] % 1000000;
    dp[i][1][0] = (dp[i][0][0] + dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % 1000000;
    dp[i][1][1] = dp[i-1][1][0] % 1000000;
    dp[i][1][2] = dp[i-1][1][1] % 1000000;
  }

  var answer = 0
  for(i: Int in 0..1) {
    for(j: Int in 0..2) {
      answer += dp[N][i][j]
    }
  }

  print(answer)
}