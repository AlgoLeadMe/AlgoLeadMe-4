// 6차시 2024.08.03.토 : 백준 - 디스크 트리(7432)
import java.io.BufferedReader
import java.io.InputStreamReader

const val DEPTH_STRING = " "

data class Node(
  var directory: String,
  var nodes: MutableList<Node>
)

var answer: StringBuilder = StringBuilder()

fun main() {
  val br = BufferedReader(InputStreamReader(System.`in`))

  val N = br.readLine().toInt()

  val root = Node("", mutableListOf())

  for(i: Int in 1..N) {
    val path = br.readLine()
    val directories = path.split("\\")

    // 트리로 정리
    var parent = root
    for(j: Int in 0..directories.size - 1) {
      val currentDirectory = directories[j]
      var index = -1

      // 부모 노드에 이미 존재하는지 확인
      for(k: Int in 0..parent.nodes.size - 1) {
        if(parent.nodes[k].directory.equals(currentDirectory)) {
          index = k
          break
        }
      }
      // 존재하지 않을 경우 자식으로 추가
      if(index == -1) {
        parent.nodes.add(Node(currentDirectory, mutableListOf()))
        index = parent.nodes.size - 1
      }
      
      // 다음 자식을 체크하기 위해 depth 증가
      parent = parent.nodes[index]
    }
  }

  root.nodes.sortBy{ it.directory }
  for(node in root.nodes) {
    tree(node, "") // depth 1
  }

  print(answer)
}

fun tree(current: Node, depth: String) {
  answer.append(depth).append(current.directory).append("\n")

  current.nodes.sortBy{ it.directory }
  for(node in current.nodes) {
    tree(node, depth + DEPTH_STRING) // Depth 증가시켜주고 자식 노드도 탐색
  }
}