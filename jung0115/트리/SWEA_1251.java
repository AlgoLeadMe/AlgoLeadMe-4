// 5차시 2024.07.31.수 : SW Expert Academy - 1251. [S/W 문제해결 응용] 4일차 - 하나로
package jung0115.트리;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;
import java.lang.Math;


public class SWEA_1251 {
  static Long[][] island;
  static int[] parents;
  private static class Edge implements Comparable<Edge> {
    int island1, island2;
    Long cost; // 비용 = 환경 부담금 (* E는 마지막에)

    Edge(int island1, int island2, Long cost) {
      this.island1 = island1;
      this.island2 = island2;
      this.cost = cost;
    }

    // 환경부담금 기준 오름차순 정렬
    @Override
    public int compareTo(Edge edge) {
      if(edge.cost < cost) return 1;
      else if(edge.cost > cost) return -1;
      return 0;
    }
  }

	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder printSet = new StringBuilder();

		int T = Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
      int N = Integer.parseInt(br.readLine()); // 섬의 개수
      island = new Long[N][2];

      // X 좌표
      StringTokenizer st = new StringTokenizer(br.readLine());
      for(int i = 0; i < N; i++) {
        island[i][0] = Long.parseLong(st.nextToken());
      }

      // Y 좌표
      st = new StringTokenizer(br.readLine());
      for(int i = 0; i < N; i++) {
        island[i][1] = Long.parseLong(st.nextToken());
      }

      Double E = Double.parseDouble(br.readLine()); // 환경 부담 세율

      // 각 섬을 잇는 해저터널의 환경 부담금 (* E는 마지막에)
      ArrayList<Edge> edges = new ArrayList<>();
      for(int i = 0; i < N; i++) {
        for(int j = i + 1; j < N; j++) {
          Long distanceX = island[i][0] - island[j][0];
          Long distanceY = island[i][1] - island[j][1];
          Long cost = (distanceX * distanceX) + (distanceY * distanceY);

          edges.add(new Edge(i, j, cost));
        }
      }

      // 환경부담금 순으로 오름차순 정렬
      Collections.sort(edges);

      // root 노드를 자기 자신으로 초기화
      parents = new int[N];
      for(int i = 0; i < N; i++) {
        parents[i] = i;
      }

      int connect = 0; // 연결된 섬의 개수
      Long totalCost = 0L; // 총 환경부담금
      for(Edge edge : edges) {
        if(isConnect(edge.island1, edge.island2)) continue;
        
        totalCost += edge.cost;
        connect++;
        if(connect == N - 1) break;
      }

      Long answer = Math.round(E * totalCost);
      printSet.append("#").append(test_case).append(" ").append(answer).append("\n");
    }

    br.close();
    System.out.print(printSet);
	}

  // 연결되어있는지 체크
  static private boolean isConnect(int island1, int island2) {
    int root1 = findRoot(island1);
    int root2 = findRoot(island2);

    if(root1 == root2) return true; // root 노드가 같다면, 이미 연결되어 있는 것
    parents[root1] = root2;
    return false;
  }

  // root 노드 찾기
  static private int findRoot(int node) {
    if(node == parents[node]) return node;
    
    parents[node] = findRoot(parents[node]);
    return parents[node];
  }
}