/*
Deadlock Detection
A few months ago, we were running a new release of our trade server in QA and experienced a hang. The system was accepting connections from clients, but no longer processing any transactions. This system is critical to many of our major trading operations and so, the issue was a big deal to fix before we released to production.
The trade server supports many different execution paths which take out various locks on shared resources.  Upon investigation, we found that the system had experienced a deadlock between two of those execution paths. To ensure we fixed the problem holistically (rather than just the deadlock case that we caught), we wanted to examine all the execution paths in the system and determine all cases that were constructed in a way that they can cause deadlocks.
We'll provide you a set of execution paths. Each is written as an ordered list of lock acquisitions. Your job is to write a program which enumerate all the subsets of sets of execution paths that could result in a deadlock if executed in parallel.
Your input will be a file with one execution path per line. The name will be first, separated by a space, then a comma separated list of the locks in order they are acquired. For instance:
    path1 L1,L2,L3
    path2 L2,L1,L3
    path3 L4,L5,L6
    path4 L5,L4,L6
Your output should be each subset of execution paths which can deadlock, one per line. Sort the paths alphabetically and order the sets alphabetically based on their lexicographic representation.
    path1,path2
    path3,path4
For more information about deadlocks, checkout the wikipedia page.
*/

import java.io.*;
import java.util.*;     //Import for Collections

public class DeadLock {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);        
        HashMap<String, List<String>> pthLck = new HashMap<String, List<String>>(); 
        
        while(sc.hasNext()){
            String data = sc.nextLine();
            String[] keyPair = data.split(" ");
            List<String> items = Arrays.asList(keyPair[1].split("\\s*,\\s*"));  //Split at commas as well as Space
            pthLck.put(keyPair[0], items);
        }        
        
        List<String> keyLst = new ArrayList<String>();
        for(String key : pthLck.keySet()){
            keyLst.add(key);
        }   
        
        Collections.sort(keyLst);
        int n = keyLst.size();
        List<String> result = new ArrayList<String>();
        
        for(String key1 : keyLst){
            int tmp = keyLst.indexOf(key1);
            for (int i = tmp+1; i<n; i++){
                String key2 = keyLst.get(i);                
                List<String> l1 = pthLck.get(key1);
                List<String> l2 = pthLck.get(key2);
                
                boolean op = checkList(l1, l2);                
                if(op){
                    String r1 = key1+","+key2;
                    result.add(r1);
                }
            }
        }
        
        for (String r2 : result)
            System.out.println(r2);        
    }
    
    public static boolean checkList(List<String> l1, List<String> l2){
        //int[] n1 = new int[l1.size()];
        int[] n2 = new int[l2.size()];
        
        for (String v1:l1){            
            int i = l1.indexOf(v1);
            
            if(l2.contains(v1)){
                int j = l2.indexOf(v1);
                //n1[i] = i;
                if(j!=i)
                    n2[j] = i;
                else if(j==i)
                    n2[j] = Integer.MAX_VALUE;
            }            
        }
        
        boolean gt = false;
        boolean lt = false;
        boolean et = false;
        
        for(int i = 0; i<n2.length; i++){
            if(i<n2[i] && n2[i]!=Integer.MAX_VALUE)
                lt = true;
            if(i>n2[i])
                gt = true;
            if(n2[i] == Integer.MAX_VALUE)
                et = true;
        }
        
        if((gt&&lt)||(lt&&et)||(gt&&et))
            return true;
        return false;
        
    }
}
/*

*/