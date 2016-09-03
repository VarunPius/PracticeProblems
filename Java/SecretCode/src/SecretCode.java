/**
 * Created by VarunPius on 8/31/2016.
 */

import java.io.*;
import java.util.HashMap;

public class SecretCode {
    public static void main(String[] args) throws IOException{
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.println("Enter Message: ");
        String ip = br.readLine();

        String[] ipmsg = ip.split("\\|");

        System.out.println("Message is: " + ipmsg[0]);

        HashMap<Character, Integer> mp = new HashMap<Character, Integer>();

        mp.put('A', 0);
        mp.put('B', 1);
        mp.put('C', 2);
        mp.put('D', 3);
        mp.put('E', 4);
        mp.put('F', 5);
        mp.put('G', 6);
        mp.put('H', 7);
        mp.put('I', 8);
        mp.put('J', 9);
        mp.put('K', 10);
        mp.put('L', 11);
        mp.put('M', 12);
        mp.put('N', 13);
        mp.put('O', 14);
        mp.put('P', 15);
        mp.put('Q', 16);
        mp.put('R', 17);
        mp.put('S', 18);
        mp.put('T', 19);
        mp.put('U', 20);
        mp.put('V', 21);
        mp.put('W', 22);
        mp.put('X', 23);
        mp.put('Y', 24);
        mp.put('Z', 25);




    }
}
