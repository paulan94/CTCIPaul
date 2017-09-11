import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class HRankArrayList {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int x = scan.nextInt();
        ArrayList<ArrayList<Integer>> myAL = new ArrayList<ArrayList<Integer>>();
        for (int i=0; i < x; i++){
            ArrayList<Integer> items = new ArrayList<Integer>();
            int d = scan.nextInt();
            if (d > 0){
                for (int j=0; j < d; j++){
                    items.add(scan.nextInt());
                }
                myAL.add(items);
            }
            else{
                ArrayList<Integer> empty = new ArrayList<Integer>();
                myAL.add(empty);
            }
        }
        int d = scan.nextInt();
        for (int k=0; k < d; k++){
            int yy = scan.nextInt()-1;
            int xx = scan.nextInt()-1;
            try{
                
                if ((myAL.get(yy).size() == 0)){
                    System.out.println("ERROR!");
                }

                else if ((myAL.get(yy).get(xx)) != null){
                     System.out.println(myAL.get(yy).get(xx));
                }

                else {
                    System.out.println("ERROR!");
                }
            }
            catch (Exception e){
                System.out.println("ERROR!");
            }
        }
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}