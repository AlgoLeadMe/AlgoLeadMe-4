// 18차시 2024.10.12.토 : 백준 - 뉴스 전하기(1135)
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

lateinit var employees: Array<MutableList<Int>>
lateinit var dp: Array<Int>

fun main() {
  val br = BufferedReader(InputStreamReader(System.`in`))

  var N = br.readLine().toInt() // 직원의 수

  val st = StringTokenizer(br.readLine())
  employees = Array(N) { mutableListOf<Int>() }
  dp = Array<Int>(N) { -1 }

  st.nextToken()
  for(i: Int in 1..N-1) {
    employees[st.nextToken().toInt()].add(i)
  }

  println(dfs(0))
}

fun dfs(employee: Int): Int {
  if (dp[employee] != -1) return dp[employee]

  // 더 이상 전화할 사람이 없음
  if (employees[employee].isEmpty()) return 0
  
  // 자식들에게 전화하는 시간
  // 내림차순 정렬
  val times = employees[employee].map { dfs(it) }.sortedDescending()

  // 각 자식에게 전화 거는 시간 계산
  var maxTime = 0
  for (i in times.indices) {
    // 자식에게 전화 + 그 자식이 전화 거는 시간
    maxTime = maxOf(maxTime, times[i] + i + 1)
  }

  dp[employee] = maxTime

  return dp[employee]
}