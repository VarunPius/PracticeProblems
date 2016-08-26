/*
 * Name: Varun Pius Rodrigues
*/

import java.io.*;
import java.util.Arrays;

public class Sorting {
    public static void main(String[] args) throws IOException{
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.println("Enter Number of numbers to be sorted: ");
        int len = Integer.parseInt(br.readLine());
        int num[] = new int[len];
        for (int i = 0; i < len; i++){
            System.out.println("Enter number:");
            num[i] = Integer.parseInt(br.readLine());
        }
        System.out.println("Numbers to be sorted are: " + Arrays.toString(num));

        /*for (int i: num){
            System.out.println(i);
        } */

        int[] bubsort = bubbleSort(num);
        System.out.println("Bubble sorted numbers are: " + Arrays.toString(bubsort));

        int[] insert_sort = InsertionSort(num);
        System.out.println("Insertion sorted numbers are: " + Arrays.toString(insert_sort));

        int[] merge_sort = MergeSort(num);
        System.out.println("Merge sorted numbers are: " + Arrays.toString(merge_sort));

        System.out.println("Numbers to be sorted are: " + Arrays.toString(num));

    }

    private static int[] bubbleSort(int[] n){
        boolean flag = true;
        int j = 0;
        int[] sortnum = Arrays.copyOf(n, n.length);
         //as sortnum = n creates a pointer to the original n as a result the original results are getting updated.
        while(flag){
            flag = false;
            j++;
            for (int i= 0; i < n.length - j; i++){
                if (sortnum[i] > sortnum[i+1]){
                    int temp = sortnum[i];
                    sortnum[i] = sortnum[i+1];
                    sortnum[i+1] = temp;
                    flag = true;
                }
            }
        }

        return sortnum;
    }

    private static int[] InsertionSort(int[] n){
        int[] sortnum = Arrays.copyOf(n, n.length);
        for(int i = 1; i<n.length; i++){
            int temp = sortnum[i];
            int j;
            for (j = i-1; j>=0 && temp < sortnum[j]; j--){
                sortnum[j+1] = sortnum[j];
            }
            sortnum[j+1] = temp;
        }
        return sortnum;
    }

    //Merge Sort begins here:
    private static int[] MergeSort(int[] n){
        int[] sortnum = Arrays.copyOf(n, n.length);
        splitPart(0, n.length-1, sortnum);
        return sortnum;
    }

    private static void splitPart(int lower_idx, int higher_idx, int[] n){
        if (lower_idx < higher_idx) {
            int middle_idx = lower_idx + (higher_idx - lower_idx) / 2;
            splitPart(lower_idx, middle_idx, n);
            splitPart(middle_idx + 1, higher_idx, n);
            mergePart(lower_idx, middle_idx, higher_idx, n);
        }
    }

    private static void mergePart(int lower_idx, int middle_idx, int higher_idx, int[] n){
        int i = lower_idx;
        int j = middle_idx + 1;
        int k = lower_idx;
        int[] tmp =  Arrays.copyOf(n, higher_idx+1);

        while (i <= middle_idx && j <= higher_idx){
            if (tmp[i] <= tmp[j]){
                n[k] = tmp[i];
                i++;
            }
            else {
                n[k] = tmp[j];
                j++;
            }
            k++;
        }

        while (i <= middle_idx) {
            n[k] = tmp[i];
            k++;
            i++;
        }
    }

    private static int[] QuickSort(int[] n){
        int[] sortnum = Arrays.copyOf(n, n.length);

        return sortnum;
    }

}
