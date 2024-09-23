// 10차시 2024.08.28.수 : 백준 - 램프(1034)
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer
import kotlin.math.max

fun main() {
  // ✅ Input
  val br = BufferedReader(InputStreamReader(System.`in`))
  var st = StringTokenizer(br.readLine())
  
  val N = st.nextToken().toInt()
  val M = st.nextToken().toInt()

  val lamp = mutableListOf<String>()
  for(i: Int in 1..N) {
    lamp.add(br.readLine())
  }

  val K = br.readLine().toInt()

  var answer = 0
  for(i: Int in 0..N-1) {
    // 꺼져있는 램프 수
    var zeroCount = 0
    for(j: Int in 0..M-1) {
      if(lamp[i][j] == '0') zeroCount++
    }

    // 불이 다 켜진 행의 수
    var rowCount = 0
    if(zeroCount <= K && zeroCount % 2 == K % 2) {
      for(j: Int in 0..N-1) {
        var isEqual = true
        for(k: Int in 0..M-1) {
          if(lamp[i][k] != lamp[j][k]) {
            isEqual = false
            break
          }
        }
        if(isEqual) rowCount++
      }

      answer = max(answer, rowCount)
    }
  }

  print(answer)
}