package nuovo;

public class Stampa extends Thread {
	
	@Override
	public void run() {
		for (int i=0; i<9; i++) {
			System.out.print(i);
		}
	}
}
