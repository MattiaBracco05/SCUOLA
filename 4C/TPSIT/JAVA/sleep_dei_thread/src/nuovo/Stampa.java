package nuovo;

public class Stampa extends Thread {
	
	@Override
	public void run() {
		int i=0;
		while(true) {
			System.out.println(i);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			i++;
		}
	}
}
