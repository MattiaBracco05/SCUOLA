package nuovo;

public class inizio {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("INIZIO");
		Stampa console1 = new Stampa();
		console1.start();
		try {
			Thread.sleep(292929);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("FINE");
	}

}
