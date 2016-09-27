package Ch03_Stack_Queue.StackMinimum;

import java.util.*;

public class StackWithMin extends Stack<WithNode>{
	private static final long serialVersionUID = 1L;

	public void push(int val){
		//int minV = this.peek().minVal;	
		int minV = Math.min(val, minStackValue());
		super.push(new WithNode(val, Math.min(val, minV)));
	}
	
	public int minStackValue(){
		if (isEmpty())
			return Integer.MAX_VALUE;
		else 
			return peek().minVal;
	}
}
