package Ch03_Stack_Queue.Animal_Shelter;

public class Cat extends Animal{
	
	public Cat(String n){
	  super(n);
	}
	
	public String name(){
	  return "Cat name is: " + name; //name here is from super class
	}
}
