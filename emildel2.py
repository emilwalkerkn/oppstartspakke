
poeng = 0
gyldige_svar = ["A", "B"]
def ugyldig():
    print("Ugyldig svar, svar enten A eller B. ")


#Den første konflikten

print("Konflikt 1: Silje og Sivert ")
print("Erling må velge mellom A og B: ")

print("A : Arranger et møte med Silje og Sivert for å diskutere konflikten")
print("B : Prioriter fremdrift og ta en beslutning på egenhånd uten å involvere de. ")

#While True gjør at spørsmålet til svar1 blir spurt om og om igjen til man sier enten A eller B.
while True:
    svar1 = input("Vil du gjøre A eller B? ").upper()
    if svar1 in gyldige_svar:
        break
    else:
        ugyldig()
if svar1 == "A":
    print("Begge parter fikk sagt sine meninger og kom til en enighet.")
    poeng += 1
elif svar1 == "B":
    print("Konflikten vokser, og samarbeidet i gruppen blir værre.")


#Den andre konflikten
print("Konflikt 2: Hamdi og Jabir ")
print("Nå må erling velge mellom A og B. ")

print("A: Arranger en workshop med både Hamdi og Jabir. ")
print("B: Velg å avvente situasjonen og håpe at de finner ut av det selv")

while True:
    svar2 = input("Velger du løsning A eller B? ").upper()
    if svar2 in gyldige_svar:
        break
    else:
        ugyldig()
if svar2 == "A":
    print("Dette bidro til en vennligere tone mellom Hamdi og Jabir. Stemningen letter og de skjønner at bde må komme til en enighet. ")
    poeng += 1
elif svar2 == "B":
    print("Konlfikten blir værre, de vil ikke snakke med hverandre og det resulterer i dårlig stemning og samarbeid i hele gruppen. ")
    

#Den tredje konflikkten
print("Konflikt 3: Sette i gang relasjonsbyggende aktiviteter? ")
print("Erling må velge mellom A og B")

print("A:  Prioritere pseudo-arbeid og relasjonsbygging. ")
print("B:  Prioritere fremdrift og resultater. ")
while True:
    svar3 = input("Vil du velge A eller B? ").upper()
    if svar3 in gyldige_svar:
        break
    else:
        ugyldig()
if svar3 == "A":
    print("Kjemien tvers av i gruppen er blitt bedre, gruppemedlemmene innser at alle er hygeglige på hver sin måte, " \
        "og det er lettere å ta opp konflikter tidlig. ")
    poeng += 1
elif svar3 == "B":
    print("Konflikter har lettere for å oppstå igjen, fordi ingen tiltak for å forhindre de er satt i gang. ")
else:
    print("Ugyldig svar")
        
if poeng == 3:
    print(f"Du fikk den beste løsningen fordi du har max score på {poeng} poeng!")
 
    print("Erling tok de riktige valgene for å vedlikeholde teamet sitt. ")
    print("Ved å bruke tid på pseudo-arbeid og konfliktløsing, har teamet blitt bedre til å samarbiede. ")
    print("Færre arbeidstimer på jobb med prioritering av pseudo-arbeid, men de timene de faktisk jobbet, ")
    print("er langt mer effektive enn hva de var før konfliktene ble håndert.")
elif poeng <= 2:
    print(f"Du fikk løsning nummer 2 fordi du hadde {poeng} ")
    print("Egenskapene dine flikthåndtering er brukbare, men ikke optimale. ")
    print("Du har tatt noen riktige valg, samt minst en feil.")
    print("Det er litt bedre samhold i gruppa, men likevell er det sjasne for at det ikke er vedvarende.")
    print("Ikke nok valg er blitt gjort for å forebygge godt samarbeid. ")
elif poeng <= 1:
    print(f"Du fikk den værste endingen fordi du fikk {poeng} poeng")
    print("Samarbiedet mellom gruppemedlemene blir værre og evnen til å produsere resultateter er blitt dårlige.")
    print("De rekker ikke fristen. ")
