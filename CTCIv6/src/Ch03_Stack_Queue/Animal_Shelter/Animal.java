package Ch03_Stack_Queue.Animal_Shelter;

public abstract class Animal {
		public String name;
		private int order;

		public Animal(String n){
			name = n;
		}

		public abstract String name();

		public void setOrder(int ord){
			order = ord;
		}

		public int getOrder(){
			return order;
		}

		public boolean isPrior(Animal a){
			return this.order < a.order;
		}

}
