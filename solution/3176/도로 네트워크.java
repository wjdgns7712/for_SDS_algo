import java.io.*;
import java.util.*;

public class Main {

    static int N, M, K;
    static int[] depth;
    static int[][] dp, min, max;
    static class E{
        int target, cost;
        public E(int target, int cost){
            this.target = target;
            this.cost = cost;
        }
    }static ArrayList<E>[] V;
    static StringBuilder sb;

    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("./input.txt")));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine()); // N 입력
        while (Math.pow(2, K)<=N) K++; // 2^K>N 인 최소 K 구하고
        // 변수 초기화
        depth = new int[N+1];
        dp = new int[N+1][K];
        min = new int[N+1][K];
        max = new int[N+1][K];
        V = new ArrayList[N+1];
        for (int i = 1; i < N+1; i++)
            V[i] = new ArrayList<>();

        for (int i = 0; i < N-1; i++) { // 양방향 간선추가
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            V[a].add(new E(b, c));
            V[b].add(new E(a, c));
        }

        dfs(1, 1); // depth 구하고
        for (int k = 1; k < K; k++) // 모든 2^k번째 부모 구하기
            for (int v = 1; v <= N; v++) {
                dp[v][k] = dp[ dp[v][k - 1] ][k - 1]; // [v]의 [2^k번째 부모]는 [v의 2^k-1번째 부모]의 [2^k-1번째 부모]
                min[v][k] = Math.min(min[v][k-1], min[ dp[v][k-1] ][ k-1 ]);
                max[v][k] = Math.max(max[v][k-1], max[ dp[v][k-1] ][ k-1 ]);
            }

        sb = new StringBuilder();
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            distance(from, to);
        }
        bw.write(sb.toString());

        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(int now, int cnt){
        depth[now] = cnt;
        for (E next : V[now])
            if(depth[next.target]==0){
                dp[next.target][0] = now;
                min[next.target][0] = next.cost;
                max[next.target][0] = next.cost;
                dfs(next.target, cnt+1);
            }
    }

    static void distance(int from, int to) {
        if (depth[from]<depth[to]){ // 무조건 from 이 더 낮은 위치에 오도록
            int tmp = from;
            from = to;
            to = tmp;
        }
        int shortest = 1000000;
        int longest = 1;
        for (int k = K-1; k >= 0; k--) { // 높이 맞춰주고
            if (Math.pow(2, k) <= depth[from]-depth[to]){
                shortest = Math.min(shortest, min[from][k]);
                longest = Math.max(longest, max[from][k]);
                from = dp[from][k];
            }
        }
        if (from==to){ // 같으면
            sb.append(shortest+" "+longest+"\n");
            return;
        }
        for (int k = K-1; k >= 0; k--) { // lca 찾을때까지
            if (dp[from][k]!=dp[to][k]){
                shortest = Math.min(shortest, Math.min(min[from][k], min[to][k]));
                longest = Math.max(longest, Math.max(max[from][k], max[to][k]));
                from = dp[from][k];
                to = dp[to][k];
            }
        }
        shortest = Math.min(shortest, Math.min(min[from][0], min[to][0]));
        longest = Math.max(longest, Math.max(max[from][0], max[to][0]));
        sb.append(shortest+" "+longest+"\n");
    }
}