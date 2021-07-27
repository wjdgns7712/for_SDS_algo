import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static int[] indegree;
    static ArrayList[] edge;
    static Queue<Integer> queue;

    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("./input.txt")));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        indegree = new int[N+1];
        edge = new ArrayList[N+1];
        for (int i = 1; i < N+1; i++) {
            edge[i]=new ArrayList<Integer>();
        }
        int a, b;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            edge[a].add(b);
            indegree[b]++;
        }

        queue = new LinkedList<Integer>();
        for (int i = 1; i < N+1; i++) {
            if (indegree[i]==0) queue.add(i);
        }

        StringBuilder sb = new StringBuilder();
        while(!queue.isEmpty()){
            int now = queue.poll();
            sb.append(now+" ");
            int size = edge[now].size();
            for (int i = 0; i < size; i++) {
                int target = (int) edge[now].get(i);
                indegree[target]--;
                if (indegree[target]==0) queue.add(target);
            }
        }
        System.out.println(sb.toString());

        br.close();
//        bw.flush();
//        bw.close();
    }
}