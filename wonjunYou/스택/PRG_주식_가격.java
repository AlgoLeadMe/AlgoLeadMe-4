package core;

import java.util.Stack;

public class PRG_주식_가격 {
  class Solution {
    public static int[] solution(int[] prices) {
      int n = prices.length;
      int[] answer = new int[n];

      Stack<Integer> stack = new Stack<>();

      for (int i = 0; i < n; i++) {
        while (!stack.isEmpty() && prices[i] < prices[stack.peek()]) {
          int j = stack.pop();
          answer[j] = i - j;
        }
        stack.push(i);
      }

      // 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우이다.
      while (!stack.isEmpty()) {
        int j = stack.pop();
        answer[j] = n - j - 1;
      }

      return answer;
    }
  }
}
