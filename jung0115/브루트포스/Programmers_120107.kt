// 22차시 2024.10.30.수 : 프로그래머스 - 점 찍기(Lv.2)
class Solution {
  fun solution(k: Int, d: Int): Long {
    var answer: Long = 0L
    val dSquare: Long = d.toLong() * d.toLong()

    for (a in 0L..d.toLong() step(k.toLong())) {
      val maxB: Long = Math.sqrt((dSquare - a * a).toDouble()).toLong() / k.toLong() + 1L
      answer += maxB
    }
    
    return answer
  }
}