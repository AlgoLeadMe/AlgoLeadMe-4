import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken()); // 집 개수
            int m = Integer.parseInt(st.nextToken()); // 도둑이 훔쳐야 하는 집의 개수
            int k = Integer.parseInt(st.nextToken()); // 방범장치가 작동하는 최소 돈의 양

            int[] amounts = new int[n];
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                amounts[j] = Integer.parseInt(st.nextToken());
            }

            int count = 0;
            int left = 0;
            int right = 0;
            int profit = 0; // 도둑이 훔친 총 금액

            // 슬라이딩 윈도우(left - right)의 간격을 m으로 고정
            while (right < m) {
                profit += amounts[right];
                right += 1;
            }

            right -= 1; // right 간격 재조정

            // 엣지 케이스 : n == m 인 경우 단 한번의 비교를 거치면 된다.
            if (n == m) {
                System.out.println(profit < k ? 1 : 0);
                continue;
            }

            while (left < n) {
                if (profit < k) {
                    count++;
                }

                profit -= amounts[left];
                left++;
                right = (right + 1) % n;
                profit += amounts[right];
            }

            System.out.println(count);
        }

    }
}
