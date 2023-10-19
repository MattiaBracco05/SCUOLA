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
### - Assegnazione del DNS server:
  -  1 Cliccare sul computer
  -  2 Cliccare su `IP Configuration`
  -  3 Nel campo `DNS Server` inserire l'indirizzo IP del mio server DNS
### - Creazione di un nome sul DNS server:
  -  1 Cliccare sul suerver
  -  2 Cliccare su `Services`
  -  3 Dal menù a sinistra cliccare su `DNS`
  -  4 Impostare il servizio su `ON`
  -  5 Selelzionare comee `type` la voce `A record` (utilizzata per gli IP V4) e inserire il nome da assegnare es. `pippo.local.pc`
  -  6 Inserire nel campo `Address` l'indirizzo IP al quale si vuole assegnare il nome
  -  7 Cliccare su `Add`
### - Visualizzazione di un file (da PC locale):
