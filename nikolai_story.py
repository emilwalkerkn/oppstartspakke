
story_state = {
    "choice_one": "",
    "choice_two": "",
    "choice_three": ""
}

#Kontekst
print ("Det har gått 6 uker siden oppstart og gruppen i sin helhet har høy motivasjon og pågang, men nå begynner elementer av teamet å nærme seg storming-fasen, der ulike perspektiver og personligheter begynner å krasje.")

#Konflikt 1 oppstår
print("-----------------------------------------------")
print ("KONFLIKT 1 – Silje og Sivert ")
print("-----------------------------------------------")
#Kontekst for konflikt 1
print ("Det er uenighet om teknologivalg og design. Konflikten har gått fra å være en sakskonflikt til en personkonflikt. \nSilje mener løsningen Sivert foreslår vil låse brukeropplevelsen og hindre innovasjon, \nmens Sivert mener Siljes forslag er urealistisk, usikkert og for kostbart. \nDiskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet.")
print(" ")

#Valg 1 oppstår og svaret lagres til senere bruk
print("\nHva skal du gjøre?")
while True:
    choice_one = input("Vil du A: Arranger et møte med Silje og Sivert for å diskutere konflikten slik at begge parter får uttrykt bekymringene sine og finne en felles løsning. \nEller B: Prioriter fremdrift og ta en beslutning på egenhånd uten å involvere de. [A/B]")
    if choice_one in ['A', 'B', 'a', 'b']:
        story_state["choice_one"] = choice_one.upper() #Lagrer inputen og normaliserer den
        break
    else:
        print ("Ugyldig input, velg enten A eller B")
print(" ")

#Historien fortsetter til konflikt 2
print("-----------------------------------------------")
print ("KONFLIKT 2 – Jabir og Hamdi ")
print("-----------------------------------------------")
#kontekst for konflikt 2
print("Samtidig med konflikten mellom Silje og Sivert oppstår det spenning mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant). \nDe er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter: ")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform, mens Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
print("Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser. Prosjektet nærmer seg en viktig milepæl: første prototype skal være klar om tre uker. \nStemningen er spent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan avgjøre om teamet beveger seg videre mot «norming» - eller blir stående fast i stormen. ")
print(" ")

#Valg 2 oppstår og svaret lagres til senere bruk
print("Hva skal du gjøre?")
while True:
    choice_two = input("Vil du A: Arranger en workshop med både Hamdi og Jabir. \nEller B: Velge å avvente situasjonen og håpe at de finner ut av det selv uten din inngripelse. [A/B]")
    if choice_two in ['A', 'B', 'a', 'b']:
        story_state["choice_two"] = choice_two.upper() #Lagrer inputen og normaliserer den
        break
    else:
        print ("Ugyldig input, velg enten A eller B")
print(" ")

#Historien fortsetter og konflikt 3 oppstår
print("-----------------------------------------------")
print("KONFLIKT 3 – Skal Erling sette i gang relasjonsbyggingsaktiviteter?")
print("-----------------------------------------------")
#Kontekst for konflikt 3
print("Relevant teori: Pseudo-arbeid (Gjøsund og Huseby, 2025). Relasjonelle kontrakter (Jacobsen, 2016). Storming fasen (Tuckman, 1965). Risikere å sitte fast i storming fasen, bør komme seg til norming fasen.")
print("Ettersom Erling ser at konflikter dukker opp, vurderer han om han skal bruke tid på å gjøre flere tiltak for å hindre nye mulige konflikter. \nKonflikter hemmer effektiviteten til engangsorganisasjonen ved å svekke tilliten og samarbeidet mellom gruppemedlemmene.")
print("Konflikten Erling står ovenfor innebærer om engangsorganisasjonen bør prioritere pseudo-arbeid og relasjonsbygging for å hindre fremtidige konflikter, eller prioritere fremdrift og resultater for å forsikre seg at de rekker tidsfristen.")
print(" ")
#Valg 3 oppstår og svaret lagres til senere bruk
while True:
    choice_three = input("Vil du A: Prioritere pseudo-arbeid og relasjonsbygging. \nEller B: Prioritere fremdrift og resultater. [A/B]")
    if choice_three in ['A', 'B', 'a', 'b']:
        story_state["choice_three"] = choice_three.upper() #Lagrer inputen og normaliserer den
        break
    else:
        print ("Ugyldig input, velg enten A eller B")

#Avslutning av historien
print(" ")
#Good ending
if story_state["choice_one"] == "A" and story_state["choice_two"] == "A" and story_state["choice_three"] == "A":
    print("God slutt: Laget ditt er kanskje ikke de som får jobben gjort fortest, men livet på arbeidsplassen er veldig hyggelig. Dere har klart å bygge et sterkt team som samarbeider godt, og dere har levert et solid produkt innen tidsfristen. Gratulerer!")
#Bad ending
elif story_state["choice_one"] == "B" and story_state["choice_two"] == "B" and story_state["choice_three"] == "B":
    print("Dårlig slutt: Prosjektet blir ferdig på rekordtid, men laget er ikke akkurat kjent for sin gode stemning. Konfliktene har skapt et giftig arbeidsmiljø, og flere teammedlemmer har sluttet. Produktet deres fungerer, men det er ikke akkurat brukervennlig. Bedre lykke neste gang!")
#Neutral endning
else:
    print("Nøytral slutt: Prosjektet deres har hatt sine oppturer og nedturer. Noen konflikter ble løst, mens andre ble ignorert. Resultatet er et produkt som fungerer, men det kunne vært bedre. Teamet deres har lært viktige leksjoner om samarbeid og konfliktløsning, som vil hjelpe dere i fremtidige prosjekter.")
