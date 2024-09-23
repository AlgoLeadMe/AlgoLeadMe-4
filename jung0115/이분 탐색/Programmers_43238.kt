// 8차시 2024.08.19.월 : 프로그래머스 - 입국심사(Lv.3)
class Solution {
  fun solution(n: Int, times: IntArray): Long {
    var min: Long = 0
    var max: Long = (times.maxOrNull()!!.toLong() * n)
    
    while (min < max) {
      val mid: Long = (min + max) / 2
      var complete: Long = 0

      for (time in times) {
        complete += mid / time
      }

      if (complete >= n) {
        max = mid
      } else {
        min = mid + 1
      }
    }
    
    return min
  }
}