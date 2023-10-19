# SIMULAZIONE SERVER DNS
## - Simulazione di un DNS server in una rete locale
## `Struttura`
- Ufficio
## `Componenti`
- Switch
- Server
## `Particolarità`
- Utilizzo del servizio DNS su un server
- Possibilità di fare un ping con il nome assegnato alla macchina
## `Comandi`
### - Assegnazione del server DNS ai computer:
  -  1 Cliccare sul computer
  -  2 Cliccare sulla scheda `IP Configuration`
  -  3 Nel campo `DNS Server` inserire l'indirizzo IP del mio server DNS
### - Assegnazione del DNS al server DNS:
  -  1 Cliccare sul server
  -  2 Cliccare sulla scheda `IP Configuration`
  -  3 Nel campo `DNS Server` inserire l'indirizzo IP del mio server DNS
### - Creazione di un nome sul server DNS:
  -  1 Cliccare sul server
  -  2 Cliccare su `Services`
  -  3 Dal menù a sinistra cliccare su `DNS`
  -  4 Impostare il servizio su `ON`
  -  5 Selelzionare comee `type` la voce `A record` (utilizzata per gli IP V4) e inserire il nome da assegnare es. `pippo.local.pc`
  -  6 Inserire nel campo `Address` l'indirizzo IP al quale si vuole assegnare il nome
  -  7 Cliccare su `Add`
### - Ping tramite nome del dispositivo:
  -  1 Cliccare sul computer
  -  2 Cliccare su `Command Prompt`
  -  3 Digitare `ping {nome assegnato al PC tramite DNS}`
### - Assegnazione di un alias tramite server DNS:
  -  1 Aprire la voce `DNS` nella scheda `Services` del mio server DNS
  -  2 Selezionare come `type` la voce `CNAME` e inserire il nome da assegnare es. `pippoPC`
  -  3 Inserire nel campo `Host Name` il nome precedentemente assegnato con il type A record (pippo.local.pc)
### - Utilizzo del comando nslookup:
  -  1 Aprire il`Prompt dei comandi` e digitare `nslookup {indirizzo del sito}` (9 es. www.denina.it)
  -  2 Mi viene resistituito l'indirizzo associato al DNS da me cercato (nel campo `Address`)
### - Utilizzo del comando nslookup in maniera interattiva:
  -  1 Aprire il `Prompt dei comandi` e digitare `nslookup`
  -  2 Digitare un DNS da ricercare es. `www.google.it`
  -  3 Digitare `exit` per uscire
