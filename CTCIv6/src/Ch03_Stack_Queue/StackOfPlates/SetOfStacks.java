package Ch03_Stack_Queue.StackOfPlates;

//import Ch03_Stack_Queue.ThreeInOne.FullStackException; 
import java.util.*;
//import java.util.EmptyStackException;

public class SetOfStacks {
	int stackCapacity;
	
	public SetOfStacks(int stackCapacity){
		this.stackCapacity = stackCapacity;
	}

	ArrayList<Stack> arrStck = new ArrayList<Stack>();

	public void push(int val) throws FullStackException{
		Stack last =  getLast();
		if(last == null || last.getSize() == stackCapacity){
			Stack newLast = new Stack(stackCapacity);
			newLast.push(val);
			arrStck.add(newLast);
		}
		else {
			last.push(val);
		}

	}
	
	public Stack getLast(){
		if(arrStck.size() == 0)
			return null;
		else
			return arrStck.get(arrStck.size() - 1);
	}

	public int pop() {
		Stack last =  getLast();
		if(last == null || last.getSize() == 0)
			throw new EmptyStackException();
		int val = last.pop();

		if(last.getSize() == 0)
			arrStck.remove(arrStck.size()-1);
		return val;
	}
	
	public void displayStackList(){
		Stack last = getLast();
		if (last != null)
			last.displayStack();
		else
			return;
		
	}

	/* 
	public int popAt(int idx){
	 
		Stack popStack = arrStck.get(idx - 1);		
		int val = popStack.pop();
		
		idx++;
		while(idx <= arrStck.size()){
			Stack newPop = arrStck.get(idx - 1);
			Stack oldPop = arrStck.get(idx);
			oldPop.push(newPop.stck[0]);
			
			//shift all elements to lower value using a separate method. 
			//Use array within a loop;
		}
		
		return val;
	}
	*/
}