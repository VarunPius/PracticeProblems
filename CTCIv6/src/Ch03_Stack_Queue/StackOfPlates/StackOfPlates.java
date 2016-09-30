package Ch03_Stack_Queue.StackOfPlates;

//import Ch03_Stack_Queue.ThreeInOne.FullStackException; 

public class StackOfPlates{

	public static void main(String[] args) throws FullStackException {
		// TODO Auto-generated method stub
		
		SetOfStacks st = new SetOfStacks(5);		
		st.push(4);
		st.push(3);
		st.push(5);
		st.push(2);
		st.push(1);
		st.push(4);
		st.push(6);
		st.push(7);
		st.push(8);
		
		System.out.println(st.pop());		
		st.displayStackList();
		System.out.println();		
		System.out.println(st.pop());		
		st.displayStackList();
		System.out.println();
		System.out.println(st.pop());		
		st.displayStackList();
		System.out.println();
		System.out.println(st.pop());		
		st.displayStackList();
		System.out.println();
		System.out.println(st.pop());		
		st.displayStackList();
		System.out.println();
		System.out.println(st.pop());		
		st.displayStackList();
	}
}
