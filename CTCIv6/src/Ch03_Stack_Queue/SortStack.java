package Ch03_Stack_Queue;

import java.util.*;
public class SortStack {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Stack<Integer> st = new Stack<Integer>();

		st.push(2);
		st.push(4);
		st.push(3);
		st.push(32);
		st.push(9);
		st.push(7);

		sort(st);

		System.out.println(st.pop());
		System.out.println(st.pop());
		System.out.println(st.pop());
		System.out.println(st.pop());
		System.out.println(st.pop());
		System.out.println(st.pop());
	}

	public static void sort(Stack<Integer> st1){
		Stack<Integer> st2 = new Stack<Integer>();

		while(!st1.empty()){
			int tmp = st1.pop();

			while(!st2.empty() && tmp > st2.peek()){
				st1.push(st2.pop());
			}
			st2.push(tmp);
		}

		while(!st2.empty()){
			st1.push(st2.pop());
		}
	}

}
