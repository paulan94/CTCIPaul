import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.PriorityQueue;

public class heapMedian {
    
    public static void insert(int number, PriorityQueue<Integer> minHeap, PriorityQueue<Integer> maxHeap){
        if (maxHeap.size() == 0 || number < maxHeap.peek()){
            maxHeap.add(number);
        } 
        else{
            minHeap.add(number);
        }
        balance(minHeap,maxHeap);
    }
    public static void balance(PriorityQueue<Integer> minHeap, PriorityQueue<Integer> maxHeap){
        if ((minHeap.size() - maxHeap.size()) > 1 ){
            //minheap has too many nodes, so move one over to maxheap
            maxHeap.add(minHeap.poll());
        }
        else if ((maxHeap.size() - minHeap.size()) > 1 ){
            //minheap has too many nodes, so move one over to maxheap
            minHeap.add(maxHeap.poll());
        }
        //if they are even, do nothing because we handle inserts in our insert function.
    }
    
    public static double findMedian(PriorityQueue<Integer> minHeap, PriorityQueue<Integer> maxHeap){
        double med;
        if (minHeap.size() > maxHeap.size()){ //case that minHeap has more elements
            med = minHeap.peek();
        }
        else if (maxHeap.size() > minHeap.size()){ //case that maxHeap has more elements
            med = maxHeap.peek();
        }
        else{                                       //case that minHeap and maxHeap have same # of elements
            med = (minHeap.peek()+maxHeap.peek())/2.0; 
        }
        return med;
    }

    public static void main(String[] args) {
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>(); //highers
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(Comparator.reverseOrder()); //lowers
        
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        double median;
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
            int number = a[a_i];
            insert(number, minHeap, maxHeap);
            median = findMedian(minHeap, maxHeap);
            System.out.println(median);
            
        }
    }
}
