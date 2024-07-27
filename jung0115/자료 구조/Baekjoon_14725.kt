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
      for(k: Int in 0..parent.nodes.size - 1) {
        if(parent.nodes[k].feed.equals(currentFeed)) {
          index = k
          break
        }
      }
      if(index == -1) {
        parent.nodes.add(Node(currentFeed, mutableListOf()))
        index = parent.nodes.size - 1
      }
      
      parent = parent.nodes[index]
    }
  }

  root.nodes.sortBy{ it.feed }
  for(node in root.nodes) {
    tree(node, "")
  }

  print(answer)
}

fun tree(current: Node, depth: String) {
  answer.append(depth).append(current.feed).append("\n")

  current.nodes.sortBy{ it.feed }
  for(node in current.nodes) {
    tree(node, depth + DEPTH_STRING)
  }
}