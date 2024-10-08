package jung0115.이분탐색;
// 15차시 2024.09.28.토 : 백준 - 가장 긴 증가하는 부분 수열 2(12015)

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon_12015 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());

    int[] A = new int[N];
    for(int i = 0; i < N; i++) {
      A[i] = Integer.parseInt(st.nextToken());
    }

    int[] longIncrease = new int[N];
    int lastIndex = 0;
    longIncrease[lastIndex] = A[0];

    for(int i = 1; i < N; i++) {
      int num = A[i];

      // 이전값보다 큼 -> 증가
      if(longIncrease[lastIndex] < num) {
        longIncrease[++lastIndex] = num;
      }
      // 이전값보다 작음
      else {
        int left = 0;
        int right = lastIndex + 1;

        while (left < right) {
          int mid = (left + right) / 2;

          if(longIncrease[mid] < num) {
            left = mid + 1;
          }
          else {
            right = mid;
          }
        }

        // num보다 작은 값 중 제일 뒤에 있는 숫자의 뒤
        longIncrease[left] = num;
      }
    }

    System.out.print(lastIndex + 1);
  }
}
