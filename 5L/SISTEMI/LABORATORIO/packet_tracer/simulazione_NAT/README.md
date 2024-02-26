# SIMULAZIONE NAT
## - Simulazione settaggio NAT
## `Componenti`
- Switch
- Router
## `Particolarità`
- Configurazione del NAT
## `Comandi`
### - Impostare NAT lato interno:
  -  1 Cliccare sul router
  -  2 Cliccare su `CLI`
  -  3 Digitare `enable` per entrare in modalità privilegiata
  -  4 Digitare `conf t` per entrare in modalita di configurazione
  -  5 Digitare `interface gigabitEthernet 0/0` per selezionare l'interfaccia
  -  6 Digitare `ip nat inside` per impostare l'interfaccia lato interno
  -  7 Digitare `exit`
### - Impostare NAT lato esterno:
  -  1 Cliccare sul router
  -  2 Cliccare su `CLI`
  -  3 Digitare `enable` per entrare in modalità privilegiata
  -  4 Digitare `conf t` per entrare in modalita di configurazione
  -  5 Digitare `interface gigabitEthernet 0/1` per selezionare l'interfaccia
  -  6 Digitare `ip nat outside` per impostare l'interfaccia lato esterno
  -  7 Digitare `exit`
### - Impostare regola NAT:
  -  1 Cliccare sul router
  -  2 Cliccare su `CLI`
  -  3 Digitare `enable` per entrare in modalità privilegiata
  -  4 Digitare `conf t` per entrare in modalita di configurazione
  -  5 Digitare `ip nat inside source static {indirizzo IP} {nuovo IP}` ad esempio `ip nat inside source static 192.168.1.1 209.165.200.254`
