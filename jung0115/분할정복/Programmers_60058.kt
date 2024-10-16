// 프로그래머스 - 괄호 변환(Lv.2)
class Solution {
  fun solution(p: String): String {
    // 괄호를 숫자로 변환
    val numP = mutableListOf<Int>()
    for(i: Int in 0..p.length - 1) {
      if(p[i] == '(') numP.add(1)
      else numP.add(-1)
    }
    
    var answerList = divideString(numP)
    
    var answer = ""
    
    for(str in answerList) {
      if(str == 1) answer += "("
      else answer += ")"
    }
    
    return answer
  }
  
  fun divideString(w: MutableList<Int>): MutableList<Int> {
    // w가 빈 문자열이거나 올바른 괄호문자열인 경우 그대로 반환
    if(w.size == 0 || isCollect(w)) return w
    
    // 균형잡힌 괄호 문자열 u, v로 분리하기
    var checkSum: Int = 0
    
    for(i: Int in 0..w.size - 1) {
      checkSum += w[i]
      
      // 균형잡힌 괄호 문자열로 나뉘는 지점
      if(checkSum == 0) {
        var u = w.subList(0, i + 1)
        val v = divideString(w.subList(i + 1, w.size).toMutableList())
        
        // u가 올바른 문자열일 경우
        if(isCollect(u)) {
          u.addAll(v)
          return u
        }
        // u가 올바른 문자열이 아닐 경우
        else {
          var result = mutableListOf<Int>()
          result.add(1)    // 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
          result.addAll(v) // 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
          result.add(-1)   // 4-3. ')'를 다시 붙입니다.
          
          // 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
          u.removeAt(0)
          u.removeAt(u.size - 1)
          for(i: Int in 0..u.size - 1) {
            u[i] *= -1
          }
          
          result.addAll(u)
          
          return result
        }
      }
    }
    
    return w
  }

  // 올바른 괄호 문자열인지 판단하는 함수
  fun isCollect(str: MutableList<Int>): Boolean {
    var checkSum: Int = 0
    for(i: Int in 0..str.size - 1) {
      checkSum += str[i]
      
      if(checkSum < 0) return false
    }
    return true
  }
}