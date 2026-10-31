class Point implements Comparable<Point> {
    int x;
    int y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    @Override
    public int compareTo(Point p) {
        int d1 = (int)Math.pow(x, 2) + (int)Math.pow(y, 2);
        int d2 = (int)Math.pow(p.x, 2) + (int)Math.pow(p.y, 2);
        return d1 - d2;
    }
    @Override
    public String toString() {
        return String.format("x=%s y=%s",x,y);
    }
}
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> pq = new PriorityQueue(Collections.reverseOrder());
        for(int[] p: points) {
            Point point = new Point(p[0], p[1]);
            pq.add(point);
            // System.out.println(pq);
            if(pq.size() > k) pq.remove();
        }
        // System.out.println(pq);
        int[][] res = new int[k][2];
        int i = 0;
        for(Point p: pq) {
            res[i][0] = p.x;
            res[i][1] = p.y;
            i++;
        }
        return res;
    }
}
