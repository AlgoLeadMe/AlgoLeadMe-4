// 9차시 2024.08.27.화 : 백준 - 음식 평론가(1188)
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Baekjoon_1188 {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());
    int N = Integer.parseInt(st.nextToken()); // 소시지의 수
    int M = Integer.parseInt(st.nextToken()); // 평론가의 수

    int answer = M - gcd(N, M);
    System.out.println(answer);
  }

  // 최대 공약수 - 유클리드 호제법
  static int gcd(int num1, int num2) {
    if(num1 % num2 == 0) return num2;
    return gcd(num2, num1 % num2);
  }
}