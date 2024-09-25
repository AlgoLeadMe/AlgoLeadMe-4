// 14차시 2024.09.25.수 : 백준 - 컵라면(1781)
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.Iterator;

public class Baekjoon_1781_fail {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int N = Integer.parseInt(br.readLine());

    HashMap<Integer, Integer> cupNoodles = new HashMap<Integer, Integer>();
    
    for(int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());

      int deadLine = Integer.parseInt(st.nextToken()); // 데드라인
      int count = Integer.parseInt(st.nextToken());    // 맞힐 때 받는 컵라면 수

      int current = cupNoodles.getOrDefault(deadLine, 0);
      if(current < count) cupNoodles.put(deadLine, count);
    }

    int answer = 0;

    Iterator<Integer> keys = cupNoodles.keySet().iterator();
    while(keys.hasNext()){
      int key = keys.next();
      answer += cupNoodles.get(key);
    }

    System.out.print(answer);
  }
}
