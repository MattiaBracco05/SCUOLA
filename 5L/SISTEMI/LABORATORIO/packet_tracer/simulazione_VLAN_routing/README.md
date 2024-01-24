# SIMULAZIONE VLAN (routing)
## - Simulazione della creazione delle VLAN
## `Struttura`
- Segreteria
- Docenti
- Tecnici
## `Componenti`
- Switch
- Router
## `Particolarità`
- Utilizzo delle VLAN con il routing (le VLAN possono comuicare fra di loro attraverso il router)
## `Comandi`
### - Interface VLAN su SW Layer 3:
  -  1 Cliccare sul router
  -  2 Cliccare sulla scheda `CLI`
  -  3 Digitare `Enable`
  -  4 Digitare `Conf t`
  -  5 Digitare `interface {Nome Dell'interfaccia}.{Numero della VLAN}` tipo `interface GigabitEthernet0/0.10`
  -  6 Digitare `encapsulation dot1Q {Numero della VLAN}` tipo `encapsulation dot1Q 10`
  -  7 Digitare `ip address {IP (default gateway) della VLAN} {Subnet Mask}` tipo `ip address 192.168.10.254 255.255.255.0`
  -  8 Digitare `Exit`  
