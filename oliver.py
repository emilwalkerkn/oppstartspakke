poeng = 0 
gyldige_svar = ["1", "2"]
def nix():
    print("Ugyldig svar, vennligst velg 1 eller 2")

#----------------------------Introduksjon-----------------------------#
print("\nGjennom forming fasen var entusiasmen innad i gruppen høy. Medlemmene i teamet var motiverte og ambisiøse, og fremgangen var stødig")
print("\nMen likt alle grupper, oppsto det eventuelle uenigheter.")

#----------------------------Konflikt 1-----------------------------#
print("\nDet oppsto en konflikt mellom Silje og Sivert, Silje mener at UXen skal prioriteres, og Sivert mener at tekniske løsninger bør komme først")
print("\nKonflikten eskaleres og går fra sak til personangrep, og det er nå opp til Erling å ta en beslutning")
print("\n Hva gjør Erling?")

print("1: Arranger et møte mellom Silje og Sivert for å de-eskalere situasjonen")
print("2: Ha tillit til at medlemmene kan løse saken selv uten innblanding")

while True:
    svar1 = input("Hvilket valg tar du? (1 eller 2): ")
    if svar1 in gyldige_svar: 
        break
    else: 
        nix()
if svar1 == "1": 
    print("\nEt kontrollert møte mellom Silje og Sivert ble arrangert, begge fikk sagt sin del og de klarte å komme til noen kompromisser.")
    poeng += 1 
elif svar1 == "2":
    print("\nKonflikten eskalerer ytterligere rett under nesa på Erling, fremdriften sakker og tilliten innad i gruppa svekkes.")

#----------------------------Konflikt 2-----------------------------#
print("\nImens konflikten til Silje og Sivert pågikk, brygget det også en uenighet mellom Jabir og Hamdi.")
print("\nHamdi ønsker en løsning gjennom bruken av kommunens eksisterende platform for å spare tid, mens Jabir ønsker en ny innovativ løsning")
print("\nKonflikten er enda bare ulmende, men Erling merker at noe er på gang og ønsker å gripe inn før det eskalerer.")
print("\nHva gjør Erling?")

print("1: Ha en demokratisk avstemning i gruppa for å finne den beste løsningen")
print("2: Ta et eget valg baser på hva du mener er best for prosjektet")

while True:
    svar2 = input("Hvilket valg tar du? (1 eller 2:) ")
    if svar2 in gyldige_svar:
        break
    else:
        nix()
if svar2 == "1":
    print("\nGjennom en demokratisk avstemning i teamet ble det klart at flertallet ønsket et valg framfor det andre, og den andre parten sier seg fornøyd")
    poeng += 1
elif svar2 == "2":
    print("\nBåde Hamdi og Jabir føler seg overkjørt av at Erling tok en beslutning bak ryggen på dem, og de retter misnøyen fra hverandre til Erling")

#----------------------------Konflikt 3-----------------------------#
print("\nEtter lang tid med negativ spenning i gruppen merker Erling at tillit og moral har truffet rock bottom")
print("\nErling føler at som prosjektleder så har han et ansvar for at alle har det bra på jobb")
print("\nHva gjør Erling?")

print("1: Dra alle ut på en karaokekveld på javell spandert av Erling")
print("2: Push alle hardere slik at prosjektet bare kan bli ferdig i tide")

while True:
    svar3 = input("Hvilket valg tar du? (1 eller 2): ")
    if svar3 in gyldige_svar:
        break
    else:
        nix()
if svar3 == "1":
    print("\nGjennom en sosial sammenkomst utenfor jobb så lettes trykket blant medlemmene litt, de klarer å sette uenighetene sine til side og har en koselig kveld sammen")
    poeng += 1
elif svar3 == "2":
    print("\nGruppa føler seg enda mer presset og misforstått og mister tilliten helt i Erling som leder.")

#----------------------------Avslutning-----------------------------#
if poeng == 3: 
    print(f"\Du fikk max score på {poeng} poeng!")
    print("\nEtter at Erling fikk løst konfliktene mellom Silje og Sivert, samt Jabir og Hamdi på en god måte, i tillegg til en koselig kveld på byen så blir jobben gjort med enda mer effektivitet gjennom god moral og godt samarbeid.")
    print("\nErling har vist seg som en god leder som tar vare på både prosjektet og teammedlemmene sine. Han er stolt over seg selv.")
elif poeng == 2:
    print(f"\nDu fikk den nest beste løsningen med {poeng} poeng.")
    print("\nErling klarte å lette på noe av trykket, og løse noen av konfliktene i gruppen, men noen medlemmer føler seg enda oversette")
    print("\nJobben blir klart gjort, men det er visse gruppemedlemmer som antagelig ikke vil jobbe med Erling i fremtiden")
elif poeng == 1: 
    print(f"\nDu fikk den tredje beste løsningen med {poeng} poeng.")
    print("\nErling presterer med under gjennomsnitlig innsats som leder.")
    print("\nDe fleste er misfornøyde, men ser enda ut til å merke noen innats fra Erling, og synes litt synd på han.")
    print("\nDet er tvilsomt at Erling blir leder for flere prosjekter i fremtiden.")
elif poeng == 0:
    print(f"\nDu fikk den dårligste løsningen med {poeng} poeng.")
    print("\nErling har mislyktes total som leder.")
    print("\nFlere av medlemmene er så misfornøyde at de går til klage på Erling")
    print("\nProsjektet blir så forsinket at det må kanselleres, og Erling mister jobben")
    print("\nDet sies at noen har sett Erling som postmann noen år i fremtiden.")





