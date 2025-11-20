# Oppstartspakke, interaksjonsoppgave fra Gruppe 7


# Variabler/dictionary
poeng = 0
story_state = {
    "choice_one": "",
    "choice_two": "",
    "choice_three": ""
}
#Konflikt 1
print("\nDet opstår en konflikt mellom Silje og Sivert i teamet ditt." \
      "Silje (UX-designer) mener at brukeropplevelsen må prioriteres høyest, "
      "mens Sivert (IT-utvikler) insisterer på at tekniske løsninger må komme først. "
     )
print("\nKonflikten eskalerer, og det begynner å påvirke teamets moral og fremdrift. " \
      "Sakskonflikten har blitt til en personlig konflikt, og de begge drar støtte av andre teammedlemmer. "
     )
print("\nSom prosjektleder må du ta en beslutning om hvordan du skal håndtere dette. "
     )
print("=*60")
print("\nHva gjør du?")
print("=60*")
print("\nA: Arranger et møte med Silje og Sivert for å diskutere konflikten, " \
      "slik at begge parter får uttrykt bekymringene sine og kan finne en felles løsning. " \
     )
print("\nB: Prioriter fremdrift og ta en beslutning på egenhånd uten å involvere de. " \
     )
#koding til konflikt 1 sal være her
while True:
    choice_one = input("\nHva gjør du? [A/B]").upper()
    if choice_one in ["A", "B"]:
       story_state["choice_one"] = choice_one
       break
    else:
        print("Ugyldig input, velg [A/B]")

if story_state["choice_one"] == "A":
    print("\nDu arrangerer et møte med Silje og Sivert. Gjennom åpen kommunikasjon og aktiv lytting, " \
          "klarer dere å finne en felles forståelse og en løsning som begge parter kan akseptere. " \
          "Teamet føler seg hørt, og samarbeidet forbedres.")
    poeng += 1
else:
     print("\nDu velger å prioritere fremdrift og tar en beslutning på egen hånd. " \
           "Du bestemmer at prosjektet må fokusere på tekniske løsninger først, " \
          "og kommuniserer dette til teamet uten å involvere Silje og Sivert i prosessen.") 
     print("Dette fører til at Silje føler seg oversett og undervurdert, "
          "noe som skaper ytterligere spenning i teamet og påvirker moralen negativt.")
input("Trykk [ENTER] for å fortsette")

print("=*60")
print("=*60")
#Konflikt 2
print("\nSamtidig som konflikten mellom Silje og Sivert, oppstår det en annen konflikt i teamet ditt. " \
      "Denne gangen er det mellom Hamdi (fra kulturavdelingen) og Jabir (brukerrepresentant). " 
     )
print("\nHamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform, " \
      "mens Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill. "
     )
print("\nForeløpig er uenigheten lavmælt, men du merker at frustrasjonen vokser. "
     )
print("\nI tillegg til uenighetene så vet du at prosjektet nærmer seg en viktig milepæl; " \
      "første prototype skal være klar om tre uker. " \
      "Stemningen er spent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan, " \
      "avgjøre om teamet beveger seg videre mot 'norming', eller blir stående fast i 'stormen'. "
      )
print("=*60")
print("\nHva gjør du?")
print("*60")
print("\nA: Arranger en workshop med både Hamdi og Jabir, " \
      "slik at de kan diskutere sine perspektiver og finne en felles vei fremover. " \
     )
print("\nB: Velg å avvente situasjonen og håpe at de finner ut av det selv, uten din inngripen. " \
     )
#koding til konflikt 2 skal være her

print("=*60")
print("=*60")
#Konflikt 3
print("\nMed bare tre uker igjen til første prototype skal leveres, merker du " \
      "at teamets motivasjon og fokus begynner å vakle. " \
      "Konfliktene som har oppstått har skapt en anspent atmosfære. " \
     )
print("\nSom prosjektleder må du ta grep for å bevare teamets moral og sikre fremdrift. " \
     )
print("=*60")
print("\nHva gjør du?")
print("*60")
print("\nA: Arranger en kort teambyggingsaktivitet for å styrke tilliten i teamet, " \
      "samtidig som du legger en klar og realistisk plan for de neste tre ukene. " \
     )
print("\nB: Fokuser på å stramme opp oppfølgingen og fremdriften, " \
      "med hyppige statusmøter og klare leveransemål. "
      )
#koding til konflikt 3 skal være her
while True:
    choice_three = input("\nHva gjør du? [A/B]").upper()
    if choice_three in ["A", "B"]:
        story_state["choice_three"] = choice_three
        break
    else: 
        print("Ugyldig valg. Vennligst velg A eller B.")

if story_state["choice_three"] == "A":
    print("\n Du arrengerer en koselig kveld utenfor jobb der medlemmene kan slappe av og legge uenighetene sine til side, dek koser seg")
    poeng += 1
else:
    print("\n Du innstrammer kravene til teamet enda mer, og de føler seg mer misforståtte og oversette. De retter misnøyen sin fra seg imellom til Erling.")

print("=*60")
print("=*60")
#Slutten
