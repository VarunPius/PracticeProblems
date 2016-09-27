package Ch03_Stack_Queue.StackMinimum;

public class StackMin {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		StackWithMin st1 = new StackWithMin();
		
		st1.push(4);
		st1.push(5);
		st1.push(3);
		st1.push(7);
		st1.push(1);
		st1.push(9);
		
		System.out.println("----------------------");
		System.out.println("----------------------");
		System.out.println("Stack with Minimum 1: ");
		System.out.println("Minimum value is: " + st1.minStackValue());
		System.out.println("Popped value is: " + st1.pop().value);
		System.out.println();
		System.out.println("Minimum value is: " + st1.minStackValue());
		System.out.println("Popped value is: " + st1.pop().value);
		System.out.println();
		System.out.println("Minimum value is: " + st1.minStackValue());
		System.out.println("Popped value is: " + st1.pop().value);
		//System.out.println();
		//System.out.println("----------------------");
		System.out.println("======================");
		
		
		StackWithMin2 st2 = new StackWithMin2();
		
		st2.push(4);
		st2.push(5);
		st2.push(3);
		st2.push(7);
		st2.push(1);
		st2.push(9);
		
		System.out.println("----------------------");
		System.out.println("----------------------");
		System.out.println("Stack with Minimum 2: ");
		System.out.println("Minimum value is: " + st2.minStackValue());
		System.out.println("Popped value is: " + st2.pop());
		System.out.println();
		System.out.println("Minimum value is: " + st2.minStackValue());
		System.out.println("Popped value is: " + st2.pop());
		System.out.println();
		System.out.println("Minimum value is: " + st2.minStackValue());
		System.out.println("Popped value is: " + st2.pop());
		//System.out.println();
		//System.out.println("----------------------");
		System.out.println("======================");

	}

}
