import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static class build{
        int inD;
        int time;
        int answer;
        ArrayList<Integer> adj;
        public build(){
            this.inD = 0;
            this.time = 0;
            this.answer = 0;
            this.adj = new ArrayList<>();
        }
    } static build[] builds;

    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("./input.txt")));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        builds = new build[N+1];
        for (int i = 1; i <= N; i++)
            builds[i] = new build();

        Queue<Integer> pq = new LinkedList<>();

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());

            builds[i].time = Integer.parseInt(st.nextToken());
            int tmp = Integer.parseInt(st.nextToken());

            if (tmp == -1)
                pq.add(i);

            while (tmp != -1){
                builds[i].inD++;
                builds[tmp].adj.add(i);
                tmp = Integer.parseInt(st.nextToken());
            }
        }

        while(!pq.isEmpty()){
            int id = pq.poll();
            builds[id].answer += builds[id].time;

            for(int adj : builds[id].adj){
                builds[adj].inD--;
                if (builds[adj].inD==0)
                    pq.add(adj);
                builds[adj].answer = Math.max(builds[adj].answer, builds[id].answer);
            }
        }
        for (int i = 1; i <= N; i++)
            bw.write(builds[i].answer+"\n");

        bw.flush();
        bw.close();
        br.close();
    }
}