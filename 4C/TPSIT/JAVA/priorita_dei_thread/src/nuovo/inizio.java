package nuovo;

public class inizio {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("INIZIO");
		Stampa console1 = new Stampa();
		Stampa console2 = new Stampa();
		console1.setPriority(1);
		console2.setPriority(2);
		console1.start();
		console2.start();
		System.out.println("FINE");
	}

}
