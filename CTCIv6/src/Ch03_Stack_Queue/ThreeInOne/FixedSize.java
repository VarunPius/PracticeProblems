package Ch03_Stack_Queue.ThreeInOne;

//import java.lang.Exception;
import java.util.EmptyStackException;

public class FixedSize {

	private int stackSize;
	private final int nosOfStacks = 3;
	int[] values;
	int[] idx;
	
	public FixedSize(int size){
		this.stackSize = size;
		values = new int[nosOfStacks * stackSize];
		idx = new int[nosOfStacks];
	}
	
	public int indexOf(int stackInd){
		int offset = (stackInd - 1)*stackSize;
		int ind = offset + idx[stackInd-1] - 1;
		return ind;
	};

	public void push(int stackInd, int val) throws FullStackException {
		if( isFull(stackInd - 1) )
			throw new FullStackException();

		idx[stackInd - 1]++;
		values[indexOf(stackInd)] = val;
		
	}

	public int pop(int stackInd){
		if( isEmpty(stackInd - 1) )
			throw new EmptyStackException();

		int val = values[indexOf(stackInd)];
		values[indexOf(stackInd)] = 0;
		idx[stackInd - 1]--;

		return val;
	}

	public boolean isFull(int stackInd){
		if (idx[stackInd] >= (stackSize) )
			return true;
		else
			return false;
	}

	public boolean isEmpty(int stackInd){
		if(idx[stackInd] == 0)
			return true;
		else 
			return false;
	}

	public int peek(int stackInd){
		if ( isEmpty(stackInd - 1) )
			throw new EmptyStackException();

		int val = values[indexOf(stackInd)];

		return val;
	}
	
	public void printStack(){
		System.out.println("----------------------------");
		System.out.println("----------------------------");
		System.out.println("Stack values in Fixed size Stack: ");
		System.out.println("----------------------------");
		for (int i = 0; i < values.length; i++){
			if(i%stackSize == 0){
				System.out.println("===");
			}
			System.out.println(values[i]);
		}
		System.out.println("----------------------------");
		System.out.println("----------------------------");
		System.out.println();
	}
}
