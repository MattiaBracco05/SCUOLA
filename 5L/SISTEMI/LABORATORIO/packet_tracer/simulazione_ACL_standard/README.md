# SIMULAZIONE ACL Standard
## - Simulazione della creazione di una ACL standard
## `Componenti`
- Switch
- Router
## `Particolarità`
- Configurazione delle ACL
## `Comandi`
### - Creazione di una ACL:
  -  1 Cliccare sul router
  -  2 Cliccare su `CLI`
  -  3 Digitare `enable` per entrare in modalità privilegiata
  -  4 Digitare `conf t` per entrare in modalita di configurazione
  -  5 Digitare `access-list {numero ACL} {permit / deny} {Indirizzo IP} {Whitecard}` ad esempio `access-list 1 permit 192.168.2.0 0.0.0.255`
  -  6 Digitare `access-list 1 deny any` per bloccare tutti gli altri pacchetti
  -  7 Digitare `interface {nome dell'interfaccia}` ad esempio `interface GigabitEthernet 0/0`
  -  8 Digitare `ip access-group {numero ACL} {in / out}` ad esempio `ip access-group 1 out`
  -  9 Digtare `exit` per terminare la configurazione dell'interfaccia
  -  10 Ripetere la procedura dai passaggi 7 a 9 per l'interfaccia `GigabitEthernet 0/1`

# SIMULAZIONE ACL Standard V2
### Modificare inoltre l'esercizio n.1 sulla ACL standard in modo da specificare una regola che impedisca il traffico dalla LAN ospiti alla LAN utenti (specificare questa volta l'IP di rete sorgente di OSPITI o UTENTE) piuttosto che l'IP di AMMINISTRAZIONE). 
