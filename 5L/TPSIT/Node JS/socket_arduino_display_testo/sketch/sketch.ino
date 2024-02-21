#include <WiFiS3.h>
#include <LiquidCrystal.h>

const int rs = 8;
const int en = 9;
const int d4 = 4;
const int d5 = 5;
const int d6 = 6;
const int d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

WiFiServer server(3000);

void setup() {
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  
  Serial.begin(115200);
  lcd.begin(16, 2); // Inizializza il display LCD 16x2
  
  server.begin();
  delay(1000);
  Serial.println("Simple WiFi");
  WiFi.begin("WIFI-STUDENTI", "WIFI-STUDENTI");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
  lcd.print("IP: ");
  lcd.print(WiFi.localIP());
}

void loop() {

  WiFiClient client = server.available();

  // se il client è connesso
  if (client) {
    Serial.print(client.remoteIP());
    lcd.setCursor(0, 1); // Imposta il cursore sulla seconda riga del display
    lcd.clear(); // Cancella il display
    
    String data = ""; // Stringa per memorizzare i dati ricevuti

    // Leggi i dati disponibili fino a quando il client non chiude la connessione
    while (client.connected()) {
      while (client.available()) {
        char c = client.read();
        data += c; // Aggiungi il carattere letto alla stringa data
      }
    }

    server.print(data); // invia la stringa ricevuta al client
    Serial.println(data); // stampa la stringa ricevuta sulla porta seriale
    lcd.print(data); // Visualizza la stringa ricevuta sul display LCD
  }
}
