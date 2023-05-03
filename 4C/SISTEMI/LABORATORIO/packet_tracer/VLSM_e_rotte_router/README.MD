# VLSM e rotte dei router

### - Simulazione di una rete con più router
- `Struttura`
- Reparto A (120 host)
- Reparto B (50 host)
- Reparto C (20 host)
- Reparto D (20 host)
- `Componenti`
- Switch
- Router
- `Particolarità`
- Organizzazione anche nella visualizzazione Physical
- Tencica di VLSM
- Settaggio delle rotte del router
- `Comandi`
- Per impostare una rotta su un router:
  - 1 Aprire la schermata del router
  - 2 digitare `enable`
  - 3 digitare `conf t` per accendere in modalità di configurazione
  - 4 digitare `ip route {ip rete destinazione} {subnet mask} {link destinazione}` nel mio caso ip route 200.100.50.192 255.255.255.224 10.10.10.2
- Per cancellare un comando errato:
  - 1 digitare il comandio errato che è stato eseguito preceduto da un `no` 
