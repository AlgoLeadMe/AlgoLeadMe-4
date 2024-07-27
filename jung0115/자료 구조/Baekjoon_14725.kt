// 4차시 2024.07.27.토 : 백준 - 개미굴(14725)
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

const val DEPTH_STRING = "--"

data class Node(
  var feed: String, // 먹이
  var nodes: MutableList<Node>
)

var answer: StringBuilder = StringBuilder()

fun main() {
  val br = BufferedReader(InputStreamReader(System.`in`))

  val N = br.readLine().toInt()

  val root = Node("", mutableListOf())
  
  for(i: Int in 1..N) {
    val st = StringTokenizer(br.readLine())
    val num = st.nextToken().toInt()

    // 트리로 정리
    var parent = root
    for(j: Int in 1..num) {
      val currentFeed = st.nextToken()
      var index = -1
      // 부모 노드에 이미 존재하는지 확인
      for(k: Int in 0..parent.nodes.size - 1) {
        if(parent.nodes[k].feed.equals(currentFeed)) {
          index = k
          break
        }
      }
      // 존재하지 않을 경우 자식으로 추가
      if(index == -1) {
        parent.nodes.add(Node(currentFeed, mutableListOf()))
        index = parent.nodes.size - 1
      }
      
      // 다음 자식을 체크하기 위해 depth 증가
      parent = parent.nodes[index]
    }
  }

  root.nodes.sortBy{ it.feed } // 자식 노드를 먹이 이름 기준으로 오름차순 정렬
  for(node in root.nodes) {
    tree(node, "")
  }

  print(answer)
}

fun tree(current: Node, depth: String) {
  answer.append(depth).append(current.feed).append("\n")

  current.nodes.sortBy{ it.feed } // 자식 노드를 먹이 이름 기준으로 오름차순 정렬
  for(node in current.nodes) {
    tree(node, depth + DEPTH_STRING) // Depth 증가시켜주고 자식 노드도 탐색
  }
}