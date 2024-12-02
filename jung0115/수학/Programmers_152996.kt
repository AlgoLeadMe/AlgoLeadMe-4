// 26차시 2024.12.02.월 : 프로그래머스 - 시소 짝꿍(Lv.2)
class Solution {
  fun solution(weights: IntArray): Long {
    var answer: Long = 0
    val weightCount = mutableMapOf<Int, Long>()

    for(weight in weights) {
      weightCount[weight] = weightCount.getOrDefault(weight, 0L) + 1
    }
    
    for((weight, count) in weightCount) {
      // 같은 무게인 사람이 2명 이상 -> 1:1로 앉을 수 있음
      if(count > 1) {
        answer += count * (count - 1) / 2
      }
      
      // 2:3 비율
      if (weight % 2 == 0 && weightCount.containsKey(weight * 3 / 2)) {
        answer += count * weightCount[weight * 3 / 2]!!
      }
      
      // 2:4 = 1:2 비율
      if (weightCount.containsKey(weight * 2)) {
        answer += count * weightCount[weight * 2]!!
      }

      // 3:4 비율
      if (weight % 3 == 0 && weightCount.containsKey(weight * 4 / 3)) {
        answer += count * weightCount[weight * 4 / 3]!!
      }
    }
    
    return answer
  }
}