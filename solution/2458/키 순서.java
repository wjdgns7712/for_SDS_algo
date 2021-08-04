import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static int[][] dist;

    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("./input.txt")));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        dist = new int[N+1][N+1];
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                dist[i][j]=999;

        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            dist[a][b] = 1;
        }
        for (int k = 1; k <= N; k++)
            for (int i = 1; i <= N; i++)
                for (int j = 1; j <= N; j++)
                    dist[i][j] = Math.min(dist[i][j], dist[i][k]+dist[k][j]);
        int answer=0;
        for (int i = 1; i <= N; i++) {
            int cnt = 0;
            for (int j = 1; j <= N; j++)
                if (dist[i][j] < 999 || dist[j][i] < 999) cnt++;
            if (cnt == N - 1) answer++;
        }
        bw.write(answer+"\n");

        bw.flush();
        bw.close();
        br.close();
    }
}