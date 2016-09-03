/**
 * Created by VarunPius on 8/31/2016.
 */

import java.io.*;
import java.util.*;

public class Colors {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.println("Enter Second Line colors: ");
        String col = br.readLine();
        String[] colArry = col.split("\\s+");
        String[] prim_col = new String[colArry.length - 1];
        for (int i = 0; i< colArry.length; i++){
            if (i == 0){
                prim_col[0] = colArry[0];
                continue;
            }

            String[] col_temp = new String[2];
            if (i < (colArry.length-1)) {
                switch (colArry[i]) {
                    case "red":
                        col_temp[0] = "blank";
                        col_temp[1] = "red";
                        break;
                    case "blue":
                        col_temp[0] = "blank";
                        col_temp[1] = "blue";
                        break;
                    case "yellow":
                        col_temp[0] = "blank";
                        col_temp[1] = "yellow";
                        break;
                    case "purple":
                        col_temp[0] = "blue";
                        col_temp[1] = "red";
                        break;
                    case "green":
                        col_temp[0] = "yellow";
                        col_temp[1] = "blue";
                        break;
                    case "orange":
                        col_temp[0] = "red";
                        col_temp[1] = "yellow";
                        break;
                    //case "blank":
                    //    col_temp[0] = "blank";
                    //    col_temp[1] = "blank";
                }

                String tmp = prim_col[i - 1];
                if (tmp == col_temp[0])
                    prim_col[i] = col_temp[1];
                else
                    prim_col[i] = col_temp[0];
            }

            if (i == (colArry.length - 1)){
                continue;
            }

        }

        for (int j = 0; j < prim_col.length; j++){
            System.out.print(prim_col[j] + " ");
        }
    }
}

//red purple green orange purple purple orange yellow yellow yellow
//  red   blue yellow   red    blue   red   yellow  blank yellow