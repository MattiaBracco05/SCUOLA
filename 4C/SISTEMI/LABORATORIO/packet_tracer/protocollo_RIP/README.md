# PROTOCOLLO RIP
## - Simulazione del protocollo RIP
## `Struttura`
4 Reti collegate fra loro da 3 Router
- Rete 1 --> 100.0.0.0
- Rete 2 --> 101.0.0.0
- Rete 3 --> 102.0.0.0
- Rete 4 --> 103.0.0.0
## `Componenti`
- Switch
- Router
## `Comandi`
### - Vedere collegamenti router:
  - 1 Apro il router e vado nella pagina CLI
  - 2 Digito `enable` (compare  il "#")
  - 3 Digito `show ip route`
### - Impostare il RIP:
  - 1 Apro il router e vado nella pagina CLI
  - 2 Digito `enable` (compare  il "#")
  - 3 Digito `conf t` per entrare in modalità configurazione
  - 4 Digiro `router rip` per entare nella configurazione del router
  - 5 Digito `version {numero versione}` per impostare la versione del rip che voglio utilizzare
    
    (nel mio caso la versione 2 perchè mi permette anche di gestire le sottoreti)
  - 6 Digito `no auto-summary`
  
    (lo imposto per poter fare il subnetting, altimenti raggrupperebbe tutto sotto un unico indirizzo IP)
  - 7 Digito `network {IP rete 1}` per impostare la prima rete
  
    (abilita il passaggio dei pacchetti)
  - 8 Digito `network {IP rete 2` per impostare la seconda rete
  - (abilita il passaggio dei pacchetti)
