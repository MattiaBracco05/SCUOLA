# SIMULAZIONE VLAN
## - Simulazione della creazione delle VLAN
## `Struttura`
- Gestione
- Vendite
- Produzione
## `Componenti`
- Switch
## `Particolarità`
- Utilizzo delle VLAN
## `Comandi`
### - Creazione di una VLAN da CLI:
  -  1 Cliccare sullo switch
  -  2 Cliccare su `CLI`
  -  3 Digitare `conf t` per entrare in modalita di configurazione
  -  4 Digitare `vlan {numero VLAN}` con il numero da assegnare alla VLAN
  -  5 Digitare `name {nome VLAN}` per assergnare un nome alla VLAN appena creata
### - Visualizzare le VLAN:
  -  1 Cliccare sullo switch
  -  2 Cliccare su `CLI`
  -  3 Digitare `show vlan brief`
### - Configurare le VLAN:
  -  1 Cliccare sullo switch
  -  2 Cliccare su `CLI`
  -  3 Digitare `conf t` per entrare in modalita di configurazione
  -  4 Digitare `interface {nome porta}` (es. fastEthernet 0/1)
  -  5 Digitare `switchport access {vlan da assegnare}` (es. vlan 10)
  -  `access` --> indica la modalità di accesso
### - Annullare un comando:
  -  1 Digitare `No {comando da annuallare}`
