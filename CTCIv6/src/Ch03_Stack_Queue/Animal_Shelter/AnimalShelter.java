package Ch03_Stack_Queue.Animal_Shelter;

public class AnimalShelter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		AnimalQueue anml = new AnimalQueue();

		anml.enqueue(new Dog("Scotch"));
		anml.enqueue(new Dog("Oreo"));
		anml.enqueue(new Cat("Maurice"));
		anml.enqueue(new Cat("Felix"));
		anml.enqueue(new Dog("Snowy"));
		anml.enqueue(new Dog("Tim"));

		System.out.println("Name for first dequeue: " + anml.dequeueAny().name());
		System.out.println("Name for first Cat: " + anml.dequeueCat().name());
		System.out.println("Name for first Dog try: " + anml.dequeueDog().name());
		System.out.println("Name for second Dog: " + anml.dequeueDog().name());
		System.out.println("Name for Second cat: " + anml.dequeueCat().name());
		System.out.println("Name for second dequeue: " + anml.dequeueAny().name());
		//System.out.println("Name for third dequeue: " + anml.dequeueAny().name());
		//Null pointer exception for last.
	}

}

/*
Name for first dequeue: Dog name is: Scotch
Name for first Cat: Cat name is: Maurice
Name for first Dog try: Dog name is: Oreo
Name for second Dog: Dog name is: Snowy
Name for Second cat: Cat name is: Felix
Name for second dequeue: Dog name is: Tim

*/
