package Ch03_Stack_Queue.ThreeInOne;

public class ThreeInOne {
	//private final int stackSize = 10; cannot make static reference to non-static variables
	//private final int nosOfStacks = 3;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		FixedSize fs = new FixedSize(5);
		fs.push(1, 11);
		fs.push(1, 12);
		fs.push(1, 13);
		fs.push(1, 14);
		fs.push(1, 15);
		//fs.push(1, 16);
		System.out.println("Stack 1 pop: " + fs.pop(1));
		System.out.println("Stack 1 pop: " + fs.pop(1));
		System.out.println("Stack 1 peek: " + fs.peek(1));
		fs.push(2, 21);
		fs.push(2, 22);
		System.out.println("Stack 2 pop: " + fs.pop(2));
		
		fs.printStack();

		
		
	}

}
