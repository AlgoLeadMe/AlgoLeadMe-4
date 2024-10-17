// 17차시 2024.10.11.금 : 프로그래머스 - 마법의 엘리베이터(Lv.2)
class Solution {
  fun solution(storey: Int): Int {
    var answer: Int = 0
    var storeyClone = storey

    while (storeyClone > 0) {
      val num = storeyClone % 10
      storeyClone /= 10

      if (num < 5) {
        answer += num
      } else if (num == 5) {
        // 5일 때, 다음 자릿수를 확인
        if (storeyClone % 10 >= 5) storeyClone++
        
        answer += 5
      } else {
        answer += (10 - num)
        storeyClone++
      }
    }

    return answer
  }
}