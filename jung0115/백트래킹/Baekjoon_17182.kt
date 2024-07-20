// 2차시 2024.07.20.토 : 백준 - 우주탐사선(17182)
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer
import java.util.LinkedList
import java.util.Queue
import kotlin.math.min

var dist: Array<Array<Int>>
//var visited: Arr

fun main() {
  // ✅ Input
  val br = BufferedReader(InputStreamReader(System.`in`))
  var st = StringTokenizer(br.readLine())

  var N: Int = st.nextToken().toInt() // 행성의 개수
  var K: Int = st.nextToken().toInt() // 발사되는 행성의 위치 = 시작점

  // 각 행성간 이동거리
  var planet = Array(N, {Array(N, {0})})
  for(i: Int in 0..N-1) {
    st = StringTokenizer(br.readLine())
    for(j: Int in 0..N-1) {
      planet[i][j] = st.nextToken().toInt()
    }
  }

  // ✅ Solve
  

  // ✅ Output
  print(answer)
}