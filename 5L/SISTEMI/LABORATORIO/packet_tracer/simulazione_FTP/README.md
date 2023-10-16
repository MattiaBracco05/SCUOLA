# SIMULAZIONE SERVER FTP
## - Simulazione della comunicazione da parte dei PC con un server FTP
## `Struttura`
- Uffcio di Topolino (con un Server FTP)
- Casa di Topolino
## `Componenti`
- Switch
- Router
- Server
## `Particolarità`
- Utilizzo del servizio FTP su un server
## `Comandi`
### - Gestione utenti su server FTP:
  -  1 Cliccare sul server
  -  2 Cliccare su `Services`
  -  3 Selezionare dalla colonna di sinstra la voce `FTP`
  -  4 Digitare uno `username` e una `password`
  -  5 Selezionare i permessi da associare all'utete
  -  6 Cliccare su `Add` per aggiungere l'utente o su `Save` per salvare le modifiche
### - Creazione di un file di testo da un PC:
  -  1 Cliccare sul PC
  -  2 Cliccare su `Desktop`
  -  3 Cliccare su `Text Editor`
  -  4 Digitare una frase di esempio `Frase di esempio simulazione FTP`
  -  5 Cliccare `CTRL + S` per salvare il file `EsempioFTP.txt`
### - Visualizzazione di un file (da PC locale):
  -  1 Cliccare sul PC
  -  2 Cliccare su `Desktop`
  -  3 Cliccare su `Command Prompt`
  -  4 Digitare `Dir`
### - Visualizzazione di un file (da server FTP):
  -  1 Cliccare sul PC
  -  2 Cliccare su `Desktop`
  -  3 Cliccare su `Command Prompt`
  -  4 Digitare `FTP {indirizzo IP del server FTP}`
  -  5 Digitare `dir` per visualizzare tutti i file presenti sul server FTP
### - Caricamento di un file sul server FTP (put):
  -  1 Connettersi al server FTP
  -  2 Digitare `put {nome del file da caricare}`
### - Scaricamento di un file sul server FTP (get):
  -  1 Connettersi al server FTP
  -  2 Digitare `get {nome del file da copiare in locale}`
### - Uscire dal terminale del server FTP per tornare al terminale del PC:
  -  1 Digitare `quit`
### - Visualizzare i comandi:
  -  1 Digitare `?`
