# ROUTER E SWITCH
## - Invio di PDU tramite comando ping a PC appartenenti alla stessa rete e a pc collegati su una rete esterna
## `Componenti`
- Switch
- Router
## `Particolarità`
 - Se il messaggio è da inviare ad un PC della stessa rete la PDU conterrà l'indirizzo MAC del PC destinatario
 - Se il messaggio è da inviare ad un PC situato in una rete esterna la PDU conterrà l'indirizzo MAC del router
## `Comandi`
### - Cambio il nome nel terminale di un dispositivo (es. dello switch):
  - 1 Apro la schermata dello switch
  - 2 Premo `INVIO` fino a visualizzare il nome con il ">"
  - 3 Digito `enable`
  - 4 Digito `conf t` per entarre in modalità di configurazione
  - 5 Digito `hostname {nome da usare}`
