package Ch03_Stack_Queue.Animal_Shelter;

import java.util.*;

public class AnimalQueue {

    LinkedList<Dog> dogList = new LinkedList<Dog>();
    LinkedList<Cat> catList = new LinkedList<Cat>();

    private int order = 0;

    public void enqueue(Animal a){
      a.setOrder(order++);
      if(a instanceof Dog){
    	  dogList.addLast((Dog) a);		//Don't Forget typecasting
      }
      else if( a instanceof Cat){
    	  catList.addLast((Cat) a);		//Don't Forget typecasting
      }
    }

    public Animal dequeueAny(){
      if(dogList.size() == 0)
        return catList.poll();
      else if(catList.size() == 0)
        return dogList.poll();

      Dog dg = dogList.peek();
      Cat ct = catList.peek();

      if(dg.isPrior(ct))
        return dogList.poll();
      else
        return catList.poll();
    }

    public Dog dequeueDog(){
      return dogList.poll();
    }

    public Cat dequeueCat(){
      return catList.poll();
    }

}
