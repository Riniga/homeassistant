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

##