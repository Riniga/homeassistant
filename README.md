# Home Assistant
Detta projekt/repo  för att kofigurera och programmera min homeassistant.
sker via repo i github, utveckling och hantering av filer kan ske i vs code på min arbetsstation
synkning sker via pull och push av filer via github




## Hantering i HomeAssitants terminal
Vi använder "Terminal & SSH" som installers via??
1. Starta terminalen under: Settings -> Apps -> Terminal & SSH
2. Öppna webbgränssnittet


### Inital konfiguration 
1. Skapa ssh-nyckelar: ssh-keygen -t ed25519
2. Lägg till public key i github under: Github -> Profile -> Settings -> SSH and GPG keys -> New SSH key
5. Testa från terminalen: ssh -T git@github.com 
6. Gå till katalogen /homeassistant
7. Anslut katalog till remote: git remote set-url origin git@github.com:Riniga/homeassistant.git
8. Verifiera: git remote -v

### Rutin för HA
Vid daglig drift, uppdateirngar etc så uppdateras data i homeassistant, denn adata kan behöva synkas över till github.
Kontroll om något uppdateras: git status -s
Add and commit: git add . && git commit -m "message" && git push origin master

Om data i github uppdaterats behöver kod hämtas
Hämta nytt från github: git pull origin master

Omstart kan behövas: 
- Kontroll att allt bör fungera: ha core check
- Starta om HA: ha core restart
