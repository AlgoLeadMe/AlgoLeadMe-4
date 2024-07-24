// 3차시 2024.07.24.수 : 백준 - 휴게소 세우기(1477)
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
  // ✅ Input
  val br = BufferedReader(InputStreamReader(System.`in`))
  var st = StringTokenizer(br.readLine())

  val N = st.nextToken().toInt() // 현재 휴게소의 개수
  var M = st.nextToken().toInt() // 더 지으려고 하는 휴게소의 개수
  val L = st.nextToken().toInt() // 고속도로의 길이

  val position = mutableListOf<Int>() // 휴게소의 위치
  position.add(0)  // 시작 위치
  position.add(L)  // 끝 위치
  st = StringTokenizer(br.readLine())
  for(i: Int in 1..N) {
    position.add(st.nextToken().toInt())
  }

  // ✅ Solve
  position.sort() // 오름차순 정렬

  var left = 1 // 0으로 하면 런타임 에러 (/ by zero) 발생
  var right = L
  while(left <= right) {
    var mid: Int = (left + right) / 2 // 최대 길이

    var cnt = 0
    // 최대 mid 길이만큼씩 떨어지게 휴게소 배치했을 때, 필요한 새 휴게소의 개수
    for(i: Int in 1..position.size - 1) {
      cnt += (position[i] - position[i - 1] - 1) / mid
      // 1을 빼주는 이유: i번 휴게소와 i-1번 휴게소 사이의 거리가 mid의 배수라면 새 휴게소가 하나 덜 필요함
    }

    // 필요한 휴게소의 개수가 M개 이상이라면, 최대 길이를 늘려야 함
    if(cnt > M) left = mid + 1
    // M개 이하라면, 더 짧은 길이를 최대로 해도 가능한지 체크하기 위해 최대 길이 줄이기
    else right = mid - 1
  }

  // ✅ Output
  print(left)
}