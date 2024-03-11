# SIMULAZIONE VPN site-to-site
## - Simulazione della creazione di una VPN site-to-site
## `Componenti`
- Switch
- Router
## `Particolarità`
- Configurazione di una VPN (di tipo site-to-site)
## `Comandi`
### - Installare pacchetti di sicurezza per IPsec (sia su R1 che su R3):
- 1 Cliccare sul router
- 2 Digitare `enable`
- 3 Digitare `conf t`
- 4 Digitare `license boot module c2900 technology-package securityko`
- 5 Digitare `exit` per uscire
- 6 Digitare `copy running-config startup-config` (`INVIO` per confermare)
- 7 Digitare `reload` per riavviare il router (`INVIO per confermare`)
