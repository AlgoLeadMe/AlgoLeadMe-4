// 21차시 2024.10.23.수 : 프로그래머스 - 여행경로(Lv.2)
class Solution {
  var N = 0

  lateinit var used: Array<Boolean>
  lateinit var cloneTickets: Array<Array<String>>
  
  lateinit var answer: Array<String>
  var answerStr: String = ""
  
  fun solution(tickets: Array<Array<String>>): Array<String> {
    val start = "ICN"
    cloneTickets = tickets.clone()
    
    N = tickets.size
    used = Array<Boolean>(N) { false }
    
    dfs(1, start, Array<String>(N + 1) { start })
    
    return answer
  }
  
  fun dfs(idx: Int, resultStr: String, result: Array<String>) {
    if(idx == N + 1) {
      if(answerStr.length == 0 || answerStr > resultStr) {
        answerStr = resultStr
        answer = result.clone()
      }
      return
    }
    
    for(i: Int in 0..N-1) {
      if(!used[i] && cloneTickets[i][0] == result[idx - 1]) {
        used[i] = true
        result[idx] = cloneTickets[i][1]
        
        dfs(idx + 1, resultStr + cloneTickets[i][1], result)
        
        used[i] = false
      }
    }
  }
}