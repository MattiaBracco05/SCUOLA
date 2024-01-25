# SIMULAZIONE VLAN (con switch di livello 3)
## - Simulazione della creazione delle VLAN
## `Struttura`
- VLAN 10
- VLAN 20
- VLAN 30
- VLAN 40
- VLAN 50
- VLAN 60
## `Componenti`
- Switch
- Switch Layer 3
- Router
## `Particolarità`
- Utilizzo delle VLAN e dello switch di livello 3 (Layer 3)
## `Comandi`
### - Interface VLAN su SW Layer 3:
  -  1 Cliccare sullo switch
  -  2 Cliccare sulla scheda `CLI`
  -  3 Digitare `Enable`
  -  4 Digitare `Conf t`
  -  5 Digitare `interface vlan 10`
  -  6 Digitare `ip address {Indirizzo IP} {Subnet Mask}` tipo `ip address 192.168.10.254 255.255.255.0`
  -  7 Digitare `Exit`
  -  8 Da rifare per tutte le VLAN (10, 20, 30, 40, 50 e 60)

### - PER ABILITARE IL ROUTING TRA LE VLAN:
  - Digitare `ip routing`

### - CONFIGURAZIONE DELLA GIGABIT ETHERNET 0/2
  -  1 Cliccare sullo switch
  -  2 Cliccare sulla scheda `CLI`
  -  3 Digitare `Enable`
  -  4 Digitare `Conf t`
  -  5 Dgitare `interface {Nome Dell'interfaccia}` tipo `interface gigabitEthernet 0/2`
  -  6 Digitare `no switchport`

### - Adesso posso configurarla come una porta del router...
- Assegno alla porta  l'IP: `192.168.100.1`
- Assegno alla porta la Subnet Mask: `255.255.255.252`