import java.io.*;
import java.util.*;

public class Main {

    static class Edge{
        int start, end, cost;
        public Edge(int s, int e, int c){
            this.start = s;
            this.end = e;
            this.cost = c;
        }
    }
    static int N, M, P[];
    static Edge[] E;

    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("./input.txt")));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(br.readLine());
        E = new Edge[M];
        P = new int[N+1];
        for (int i = 1; i <= N; i++) {
            P[i]=i;
        }

        String[] str;
        int s, e, c;
        for (int i = 0; i < M; i++) {
            str = br.readLine().split(" ");
            s = Integer.parseInt(str[0]);
            e = Integer.parseInt(str[1]);
            c = Integer.parseInt(str[2]);
            E[i] = new Edge(s, e, c);
        }
        Arrays.sort(E, (a,b)-> a.cost-b.cost);

        int lines = 0;
        int answer = 0;
        for (int i = 0; i < M; i++) {
            if (lines==N-1) break;

            if (union(E[i].start, E[i].end)){
                answer+=E[i].cost;
            }
        }
        System.out.println(answer);

        br.close();
        bw.flush();
        bw.close();
    }

    public static boolean union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if(pa==pb) return false;
        P[pa]=pb;
        return true;
    }
    public static int find(int a){
        if(a==P[a]) return a;
        return P[a]=find(P[a]);
    }
}