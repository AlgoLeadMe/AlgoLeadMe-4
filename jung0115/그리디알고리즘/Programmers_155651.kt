// 25차시 2024.11.27.수 : 프로그래머스 - 호텔 대실(Lv.2)
import java.util.Arrays

class Solution {
  fun solution(book_time: Array<Array<String>>): Int {
    val times = IntArray(1440)

    for (time in book_time) {
      var start = time[0].substring(0, 2).toInt() * 60 + time[0].substring(3, 5).toInt()
      var end = time[1].substring(0, 2).toInt() * 60 + time[1].substring(3, 5).toInt()
      
      for (j in start until (end + 10).coerceAtMost(1440)) {
        times[j]++
      }
    }

    return times.maxOrNull() ?: 0
  }
}