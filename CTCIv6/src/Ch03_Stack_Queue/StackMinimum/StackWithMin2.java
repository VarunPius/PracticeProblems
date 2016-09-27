package Ch03_Stack_Queue.StackMinimum;

import java.util.*;

public class StackWithMin2 extends Stack<Integer>{
	private static final long serialVersionUID = 1L;
	
	//int nos;
		
	Stack<Integer> minStack = new Stack<Integer>();
	
	public void push(int val){
		super.push(val);
		
		if(val < minStackValue() ){
			minStack.push(val);
		}		
	};
	
	public int minStackValue(){
		if(minStack.isEmpty())
			return Integer.MAX_VALUE;
		else 
			return minStack.peek();
	}
	
	public Integer pop(){
		int val;
		if (isEmpty())
			return Integer.MAX_VALUE;
		else {
			val = super.pop();
		}
		
		if (val == minStack.peek())
			minStack.pop();
		
		return val;			
	}
}
