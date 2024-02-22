# SIMULAZIONE ACL Estesa
## - Simulazione della creazione di una ACL estesa
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
  -  5 Digitare `access-list {numero ACl} {permit / deny} {protocollo} host {IP host partenza} host {IP host arrivo} eq {numero porta}` ad esempio `access-list 110 permit tcp host 192.168.3.1 host 192.168.1.100 eq 80`
  -  6 Digitare `access-list {numero ACL} {permit / deny} ip any any` ad esempio `access-list 110 deny ip any any`
  -  7 Digitare `interface {nome dell'interfaccia}` ad esempio `interface GigabitEthernet 0/0`
  -  8 Digitare `ip access-group {numero ACL} {in / out}` ad esempio `ip access-group 110 out`
  -  9 Cliccare `CTRL + Z` per terminare la configurazione dell'interfaccia
