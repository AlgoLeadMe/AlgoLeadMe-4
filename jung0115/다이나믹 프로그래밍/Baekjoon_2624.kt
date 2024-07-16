// 1차시 2024.07.16.화 : 백준 - 동전 바꿔주기(2624)
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
  // ✅ Input
  val br = BufferedReader(InputStreamReader(System.`in`))

  var T = br.readLine().toInt() // 지폐의 금액
  var K = br.readLine().toInt() // 동전의 가지 수

  var coins = Array(K, {Array(2, {0})})

  // 동전의 금액과 개수
  for(i: Int in 0..K-1) {
    val st = StringTokenizer(br.readLine())
    coins[i][0] = st.nextToken().toInt()
    coins[i][1] = st.nextToken().toInt()
  }

  // ✅ Solve
  // [몇 번째 동전까지 사용했는지][만드는 금액]
  var dp = Array(K + 1, {Array(T+1, {0})})
  for(i: Int in 1..K) { // 현재 사용하려는 동전 번호
    dp[i - 1][0] = 1
    for(money: Int in 1..T) { // 만드는 금액
      for(cnt: Int in 0..coins[i - 1][1]) { // i번째 동전의 개수
        if(money < coins[i - 1][0] * cnt) break
        dp[i][money] += dp[i - 1][money - coins[i - 1][0] * cnt]
      }
    }
  }

  // ✅ Output
  print(dp[K][T])
}