// 7차시 2024.08.07.수 : 프로그래머스 - 지형 이동(Lv.4)
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
  public int solution(int[][] land, int height) {
    int answer = 0;
    int N = land.length;
    
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    
    boolean[][] visited = new boolean[N][N];
    
    // 우선순위 큐
    Queue<Point> queue = new PriorityQueue<>();
    queue.add(new Point(0, 0, 0));
    
    while (!queue.isEmpty()) {
      Point current = queue.poll();
      
      // 이미 방문한 곳
      if (visited[current.x][current.y]) continue;
      
      // 방문 표시, 비용 추가
      visited[current.x][current.y] = true;
      answer += current.cost;

      // 상하좌우 이동
      for (int i = 0; i < 4; i++) {
        int moveX = current.x + dx[i];
        int moveY = current.y + dy[i];
        
        // 범위를 벗어나는 경우
        if (moveX < 0 || moveY < 0 || moveX >= N || moveY >= N) continue;
        
        // 높이 차이
        int cost = Math.abs(land[current.x][current.y] - land[moveX][moveY]);
        
        // 사다리가 필요한 경우
        if (cost > height) {
          queue.add(new Point(moveX, moveY, cost));
          continue;
        }
        
        // 사다리가 필요없는 경우
        queue.add(new Point(moveX, moveY, 0));
      }
    }


    return answer;
  }
  
  class Point implements Comparable<Point> {
    int x;
    int y;
    int cost;

    public Point(int x, int y, int cost) {
      this.x = x;
      this.y = y;
      this.cost = cost;
    }

    // 우선순위: 비용이 작은 순
    @Override
    public int compareTo(Point o) {
      return this.cost - o.cost;
    }
  }
}