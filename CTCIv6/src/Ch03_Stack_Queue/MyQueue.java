package Ch03_Stack_Queue;

import java.util.*;

public class MyQueue {
	
	public static Stack<Integer> stackNew = new Stack<Integer>();
	public static Stack<Integer> stackOld = new Stack<Integer>();

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		add(5);
		add(4);
		add(3);
		add(2);
		add(1);

		System.out.println("Peeked value: " + peek());
		System.out.println("Popped value: " + remove());
		System.out.println("Popped value: " + remove());
		System.out.println("Peeked value: " + peek());
		System.out.println("Popped value: " + remove());

	}
	
	public static int getSize(){
		return stackOld.size() + stackNew.size();
	}

	public static void add(int val){
		stackNew.push(val);
	}

	public static void shiftData(){
		if(stackOld.empty()){
			while(!stackNew.empty()){
				int tmp = stackNew.pop();
				stackOld.push(tmp);
			}
		}
	}

	public static int peek(){
		shiftData();
		return stackOld.peek();
	}

	public static int remove(){
		shiftData();
		return stackOld.pop();
	}

}
