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
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `license boot module c2900 technology-package securityko`
- 6 Digitare `exit` per uscire
- 7 Digitare `copy running-config startup-config` (`INVIO` per confermare)
- 8 Digitare `reload` per riavviare il router (`INVIO` per confermare)

## Configurazioni sul router R1

### - Attivare la VPN per il traffico tra le due LAN aziendali (su R1):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `access-list {numero ACL} {permit/deny} ip {IP sorgennte} {white card} {IP destinazione} {white card}` ad esempio `access-list 110 permit ip 192.168.1.0 0.0.0.255 192.168.3.0 0.0.0.255`

### - Configurazione della Fase-1 (su R1):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `crypto isakmp policy 10`
- 6 Digitare `encryption aes`
- 7 Digitare `authentication pre-share`
- 8 Digitare `group 2`
- 9 Digitare `exit`
- 10 Digitare `crypto isakmp key cisco address 10.2.2.2`
  
### - Configurazione della Fase-2 (su R1):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `crypto ipsec transform-set VPN-SET esp-3des esp-sha-hmac`
- 6 Digitare `crypto map VPN-MAP 10 ipsec-isakmp`
- 7 Digitare `description VPN connection to R3`
- 8 Digitare `set peer 10.2.2.2`
- 9 Digitare `set transform-set VPN-SET`
- 10 Digitare `match address 110`
- 11 Digitare `exit`

### - Associare la VPN con l’interfaccia seriale s0/0/0 (su R1):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `interface S0/0/0`
- 6 Digitare `crypto map VPN-MAP`

## Configurazioni sul router R3

### - Attivare la VPN per il traffico tra le due LAN aziendali (su R3):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `access-list 110 permit ip 192.168.3.0 0.0.0.255 192.168.1.0 0.0.0.255`

### - Configurazione della Fase-1 (su R3):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `crypto isakmp policy 10`
- 6 Digitare `encryption aes`
- 7 Digitare `authentication pre-share`
- 8 Digitare `group 2`
- 9 Digitare `exit`
- 10 Digitare `crypto isakmp key cisco address 10.2.2.2`

### - Configurazione della Fase-2 (su R3):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `crypto ipsec transform-set VPN-SET esp-3des esp-sha-hmac`
- 6 Digitare `crypto map VPN-MAP 10 ipsec-isakmp`
- 7 Digitare `description VPN connection to R1`
- 8 Digitare `set peer 10.1.1.2`
- 9 Digitare `set transform-set VPN-SET`
- 10 Digitare `match address 110`
- 11 Digitare `exit`

### - Associare la VPN con l’interfaccia seriale s0/0/1 (su R3):
- 1 Cliccare sul router
- 2 Andare sulla scheda `CLI`
- 3 Digitare `enable`
- 4 Digitare `conf t`
- 5 Digitare `interface S0/0/1`
- 6 Digitare `crypto map VPN-MAP`
