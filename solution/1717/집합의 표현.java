import java.io.*;
import java.util.*;

public class Main {
    static int[] arr;
    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("./input.txt")));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        arr = new int[N+1];
        for (int i = 0; i < N+1; i++)
            arr[i]=i;
        for (int i = 0; i < M; i++) {
            String[] str = br.readLine().split(" ");
            if (str[0].equals("0"))
                union(Integer.parseInt(str[1]), Integer.parseInt(str[2]));
            else{
                if (find(Integer.parseInt(str[1]))==find(Integer.parseInt(str[2])))
                    bw.write("YES\n");
                else
                    bw.write("NO\n");
            }
        }
        br.close();
        bw.flush();
        bw.close();
    }
    private static void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        arr[Math.max(pa, pb)]=Math.min(pa, pb);
    }
    private static int find(int a) {
        if (arr[a]==a) return a;
        return arr[a]=find(arr[a]);
    }
}