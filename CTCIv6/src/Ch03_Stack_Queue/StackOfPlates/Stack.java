package Ch03_Stack_Queue.StackOfPlates;

//import FullStackException;
import java.util.EmptyStackException;

public class Stack {
	
	int capacity;
	int size;
	int stck[]; // = new int[capacity];	
	
	public Stack(int capacity){
		this.capacity = capacity;
		size = 0;
		stck = new int[capacity];
	}
	
	
	
	public void push(int val) throws FullStackException {
		if(size >= capacity)
			throw new FullStackException();
		else{
			stck[size++] = val;
			//size++;
		}
	}
	
	public int pop(){
		if (size == 0)
			throw new EmptyStackException();
		
		size--;
		int val = stck[size];
		stck[size] = 0;
		return val;	
	}
	
	public int getSize(){
		return size;
	}
	
	public void displayStack(){
		System.out.println("Stack values:");
		for (int i = 0; i < size; i++){
			System.out.println(stck[i]);
		}
	}
}
