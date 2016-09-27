package Ch03_Stack_Queue.ThreeInOne;

public class FullStackException extends Exception {
	private static final long serialVersionUID = 1L;
	public FullStackException(){
        super();
        System.out.println("Stack full error");
    }

    public FullStackException(String message){
        super(message);
    }
}
