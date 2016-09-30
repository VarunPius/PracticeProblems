package Ch03_Stack_Queue.Animal_Shelter;

public class Dog extends Animal{

    public Dog(String n){
      super(n);
    }

    public String name(){
      return "Dog name is: " + name; //name here is from super class
    }
}
