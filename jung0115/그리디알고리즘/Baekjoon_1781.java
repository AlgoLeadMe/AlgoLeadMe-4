// 14차시 2024.09.25.수 : 백준 - 컵라면(1781)
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Baekjoon_1781 {
  static class CupNoodle implements Comparable<CupNoodle> {
    int deadLine;
    int count;

    public CupNoodle(int deadLine, int count) {
      this.deadLine = deadLine;
      this.count = count;
    }

    @Override
    public int compareTo(CupNoodle o) {
      // 데드라인을 기준으로 오름차순 정렬
      return this.deadLine - o.deadLine;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int N = Integer.parseInt(br.readLine());

    CupNoodle[] cupNoodles = new CupNoodle[N];
    
    for (int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());

      int deadLine = Integer.parseInt(st.nextToken()); // 데드라인
      int count = Integer.parseInt(st.nextToken());    // 맞힐 때 받는 컵라면 수

      cupNoodles[i] = new CupNoodle(deadLine, count);
    }

    // 데드라인을 기준으로 정렬 (오름차순)
    Arrays.sort(cupNoodles);

    PriorityQueue<Integer> pq = new PriorityQueue<>();

    for (CupNoodle cn : cupNoodles) {
      // 만약 현재 데드라인 내에 풀 수 있는 문제라면 큐에 추가
      pq.offer(cn.count);
      
      // 큐의 크기가 데드라인을 초과하면 가장 적은 컵라면 수를 제거
      if (pq.size() > cn.deadLine) {
        pq.poll();
      }
    }

    int answer = 0;

    // 큐에 남아 있는 컵라면의 총합을 구함
    while (!pq.isEmpty()) {
      answer += pq.poll();
    }

    System.out.println(answer);
  }
}
