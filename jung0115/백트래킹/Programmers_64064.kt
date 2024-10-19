// 20차시 2024.10.19.토 : 프로그래머스 - 불량 사용자(Lv.3)
import java.util.HashSet

class Solution {
  lateinit var userIdsClone: Array<String>
  lateinit var bannedIdsClone: Array<String>
  lateinit var collectIds: Array<MutableList<String>>
  
  val answer = HashSet<HashSet<String>>()
  
  fun solution(user_id: Array<String>, banned_id: Array<String>): Int {
    userIdsClone = user_id.clone()
    bannedIdsClone = banned_id.clone()
    
    collectIds = Array(banned_id.size) { mutableListOf<String>() }
    
    // banned_id에 각각 올 수 있는 user_id 찾기
    for(i: Int in 0..banned_id.size - 1) {
      for(j: Int in 0..user_id.size - 1) {
        if(isCollect(banned_id[i], user_id[j])) {
          collectIds[i].add(user_id[j])
        }
      }
    }
    
    dfs(HashSet<String>(), 0)
    
    return answer.size
  }
  
  fun dfs(set: HashSet<String>, cnt: Int) {
    if(cnt == collectIds.size) {
      answer.add(HashSet(set))
      return
    }
    
    for(userId in collectIds[cnt]) {
      if(set.contains(userId)) continue
      
      set.add(userId)
      dfs(set, cnt + 1)
      set.remove(userId)
    }
  }
  
  fun isCollect(bannedId: String, userId: String): Boolean {
    if(bannedId.length != userId.length) return false
    
    for(i: Int in 0..bannedId.length - 1) {
      if(bannedId[i] != '*' && bannedId[i] != userId[i]) {
        return false
      }
    }
    
    return true
  }
}