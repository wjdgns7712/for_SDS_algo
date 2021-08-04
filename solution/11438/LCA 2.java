import java.io.*;
import java.util.*;

public class Main {

    static int N, M, K;
    static int[] depth;
    static int[][] dp;
    static ArrayList<Integer>[] nodes;

    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("./input.txt")));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        depth = new int[N+1];
        nodes = new ArrayList[N+1];
        while(Math.pow(2, K)<=N) K++;
        dp = new int[N+1][K]; // N번째 노드의 2^K번째 부모노드

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (nodes[a]==null) nodes[a] = new ArrayList<>();
            if (nodes[b]==null) nodes[b] = new ArrayList<>();
            nodes[a].add(b);
            nodes[b].add(a);
        }

        dfs(1, 1);
        for (int k = 1; k < K; k++) // v보다 k가 먼저 수행되어야함!
            for (int v = 1; v <= N; v++)
                dp[v][k] = dp[ dp[v][k-1] ][ k-1 ]; // [v]의 [2^k번째 부모]는 [v의 k-1번째 부모]의 [k-1번째 부모]

        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            bw.write(lca(a, b)+"\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
    public static void dfs(int id, int dep){
        depth[id]=dep;
        for (int i = 0; i < nodes[id].size(); i++) {
            int next = nodes[id].get(i);
            if (depth[next]==0){
                dp[next][0]=id;
                dfs(next, dep+1);
            }
        }
    }
    public static int lca(int a, int b){
        if (depth[a]<depth[b]){ // 무조건 a가 b보다 낮은위치에 오도록 바꿔주기.
            int tmp=a;
            a=b;
            b=tmp;
        }
        for (int i = K-1; depth[a]>depth[b]; i--) // 같은 depth로 맞춰주기.
            if (Math.pow(2, i) <= depth[a]-depth[b])
                a = dp[a][i];
        if (a==b) return a; // 같은 depth인데 값이 같으면 바로 return LCA
        for (int i = K-1; i>=0; i--) // 아니면 LCA바로 밑까지 둘다 올려주기
            if (dp[a][i]!=dp[b][i]){
                a = dp[a][i];
                b = dp[b][i];
            }
        return dp[a][0]; // return LCA
    }
}