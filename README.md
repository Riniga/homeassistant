# Home Assistant
Detta projekt använder jag för att kofigurera och programmera min homeassistant.


## Terminal och hämta i Home Assistant
Starta terminalen under: Settings -> Apps -> Terminal

### SSH-Key för access till github
1. kör ssh-keygen -t ed25519
2. Öppna: Github -> Profile -> Settings -> SSH and GPG keys -> New SSH key
3. Lägg till namn och public key från homeassistant.
4. Testa från terminalen: ssh -T git@github.com 
5. Gå till katalogen /homeassistant
6. Kör: git remote set-url origin git@github.com:Riniga/homeassistant.git
7. Verifiera: git remote -v

### Hantering
Från HA gör push och pull så att den är uppdaterad
Vid pull kan omstart behövas
- Kontroll: ha core check
- Omstart: ha core restart

##


## Dashboards
En dashboard ska svara på en fråga.

Vi skall använda: Home Assistant Minimalist


## Dashboard 3 - Energi
Fråga: Vad kostar huset att driva?
Visar:
Elpris nu
Kostnad idag
Kostnad månad
Förbrukning
Historik

## Dashboard 4 - Säkerhet
Fråga: Är huset säkert?
Visar:
Dörrar
Fönster
Kameror
Larm

## Dashboard 5 - Teknik
Målgrupp: Rickard
Visar:
MQTT
ESPHome
UniFi
Zigbee
Matter
Batterier
Offline-enheter

Ingen annan behöver se den.

## Dashboard 6 - Städning & Automation
Framtida dashboard.
Visar:
Familjen hemma
Dammsugare
Scheman
Automationer