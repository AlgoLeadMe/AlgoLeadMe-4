// 2차시 2024.07.20.토 : 백준 - 우주탐사선(17182)
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer
import kotlin.math.min

var N: Int = 0
var K: Int = 0
lateinit var planet: Array<Array<Int>>
lateinit var visited: Array<Boolean>
var answer = Integer.MAX_VALUE

fun main() {
  // ✅ Input
  val br = BufferedReader(InputStreamReader(System.`in`))
  var st = StringTokenizer(br.readLine())

  N = st.nextToken().toInt() // 행성의 개수
  K = st.nextToken().toInt() // 발사되는 행성의 위치 = 시작점

  // 각 행성간 이동거리
  planet = Array(N, {Array(N, {0})})
  for(i: Int in 0..N-1) {
    st = StringTokenizer(br.readLine())
    for(j: Int in 0..N-1) {
      planet[i][j] = st.nextToken().toInt()
    }
  }

  // ✅ Solve
  visited = Array(N, {false})
  for(k: Int in 0..N-1) {
    for(i: Int in 0..N-1) {
      for(j: Int in 0..N-1) {
        if(i == j) continue // 출발과 도착이 같으면 패스
        // i에서 j로 바로 가는 것과 k를 거쳐서 가는 것 중 더 빠른 길을 저장
        planet[i][j] = min(planet[i][j], planet[i][k] + planet[k][j])
      }
    }
  }

  visited[K] = true
  dfs(1, K, 0)

  // ✅ Output
  print(answer)
}

// ✅ Solve
fun dfs(visitCnt: Int, position: Int, time: Int) {
  if(visitCnt == N) {
    answer = min(answer, time)
    return
  }

  for(i: Int in 0..N-1) {
    if(!visited[i]) {
      visited[i] = true
      dfs(visitCnt + 1, i, time + planet[position][i])
      visited[i] = false
    }
  }
}