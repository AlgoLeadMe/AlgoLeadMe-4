import java.util.*;

class Solution {
    static int[][] network;

    public int solution(int n, int[][] wires) {
        int minDifference = n;
        network = new int[n+1][n+1];

        for(int i = 0; i < wires.length; i++){
            int start = wires[i][0], end = wires[i][1];
            network[start][end] = 1;
            network[end][start] = 1;
        }

        for(int i = 0; i < wires.length; i++){
            int start = wires[i][0], end = wires[i][1];
            network[start][end] = 0;
            network[end][start] = 0;

            minDifference = Math.min(minDifference, bfs(n, start));
            network[start][end] = 1;
            network[end][start] = 1;
        }
        return minDifference;
    }

    public static int bfs(int n, int startNode){
        boolean[] visited = new boolean[n+1];
        int count = 1;

        Queue<Integer> queue = new LinkedList<>();
        visited[startNode] = true;
        queue.offer(startNode);

        while(!queue.isEmpty()){
            int currentNode = queue.poll();

            for(int i = 1; i <= n; i++){
                if(network[currentNode][i] == 1 && !visited[i]){
                    visited[i] = true;
                    queue.offer(i);
                    count++;
                }
            }
        }

        return Math.abs(count - (n - count));
    }
}
