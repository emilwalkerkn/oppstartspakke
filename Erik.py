#---Main storyline---
# This is the main storyline for Gruppeinnlevering 2, Erling&CO project.

print("Det har gått 6 uker siden oppstart og gruppen i sin helhet har høy motivasjon og pågang, men nå begynner elementer av teamet å nærme seg stormingfasen, der ulike perspektiver og personligheter begynner å kræsje.")
#---Konflikt 1---
print ("Konflikt 1: Silje og Sivert. Det er uenighet om teknologivalg og design. Konflikten har gått fra å være en sakskonflikt til en personkonflikt.")
print ("Silje mener løsningen Sivert foreslår vil låse  brukeropplevelsen og hindre innovasjon")
print ("Sivert mener Siljes forslag er urealistisk, usikkert og for kostbart.")
print ("Diskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet")
#---Løsning 1---
print ("Valg 1: Arranger et møte med Silje og Sivert for å diskutere konflikten slik, " \
       "at begge parter får utrykke sine bekymringer og finne en felles løsning.")
print ("Valg 2: Prioriter fremdrift og ta en bestlutning uten å involvere Silje og Sivert")
#---utfall basert på valg---
valg = input("Velg 1 eller 2 for å se utfallet av valget ditt: ")
if valg == "1":
    print ("Utfallet av valg 1: Møtet gir begge parter en mulighet til å lufte sine bekymringer, " \
              "og de klarer å finne en kompromiss som ivaretar begge sine behov.")
elif valg == "2":
    print ("Utfallet av valg 2: Silje og Sivert føler seg oversett og misforstått, " \
              "noe som fører til økt spenning i teamet og redusert motivasjon.")
#---Konflikt 2---
print ("Konflikt 2: Jabir og Hamdi. Samtidig med konflikten mellom Silje og Sivert, " \
       "oppstår det spenning mellom Jabir og Hamdi, de er uenig om hvordan innbyggerne, " \
       "skal kunne delta i digitale folkemøter.")
print ("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
print ("Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
print ("Foreløpig er uenigheten lavmælt, men Erling merker at frustasjonen vokser. Prosjektet, " \
       "nærmer seg en viktig milepæl, første prototype skal være klar om tre uker. Stemningen, " \
       " er spent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan avgjøre, " \
       "om teamet beveger seg videre mot norming, eller blir stående fast i stormingfasen.")
#---Løsning 2---
print ("Valg 1: Arranger en workshop med Jabir og Hamdi for å høre begges meninger, " \
       "og finne en løsning som kombinerer deres ideer.")
print ("Valg 2: Velg å avvente situasjonen og håpe at de finner ut av en løsning på egenhånd.")
#---utfall basert på valg---
valg2 = input("Velg 1 eller 2 for å se utfallet av valget ditt: ")
if valg2 == "1":
       print ("Utfallet av valg 1: Workshopen gir Jabir og Hamdi en mulighet til å forstå hverandres perspektiver, " \
                     "og de klarer å finne en løsning begge er tilfreds med.")
elif valg2 == "2":
       print ("Utfallet av valg 2: Uenigheten mellom Jabir og Hamdi eskalerer, " \
                     "og de begynner å bli enda mer frustrerte, noe som sakker ned fremdriten i prosjektet.")
#---konflikt 3---
print ("Konflikt 3: Ettersom at Erling ser at konflikter dukker opp, vurderer han, "\
       "om han skal bruke tid på å gjøre flere tiltak for å hindre nye mulige konflikter.")
print ("Konflikter hemmer effektiviteten til engangsorganisasjonen ved å svekke tilliten, " \
       "og samarbeidet mellom gruppemedlemmene.")
print ("Konflikten Erling står ovenfor innebærer om engangsorganisasjonen bør, " \
       "prioritere pseudo-arbeid og relasjosnbygging for å hindre fremtidige konflikter, " \
       "eller prioritere fremdrift og resultater for å forsikre seg at de rekker tidsfristen.")
#---Løsning 3---
print ("Valg 1: Prioritere pseudo-arbeid og relasjonsbygging")
print ("Valg 2: Prioritere fremdrift og resultater")
#---utfall basert på valg---
valg3 = input("Velg 1 eller 2 for å se utfallet av valget ditt: ")
if valg3 == "1":
    print ("Utfallet av valg 1: Ved å prioritere pseudo-arbeid og relasjonsbygging, " \
           "klarer Erling å skape et mer sammensveiset team som er bedre rustet til å håndtere konflikter.")
elif valg3 == "2":
    print ("Utfallet av valg 2: Ved å prioritere fremdrift og resultater, " \
           "klarer Erling å holde prosjektet på sporet, men teamets moral og samarbeid, " \
        "blir svekket, noe som kan føre til flere konflikter i fremtiden.")
#---avslutning basert på poeng---
# beregn totalpoeng ut fra de tre valgene (hvert valg er "1" eller "2")
total_poeng = 0
try:
    total_poeng = int(valg) + int(valg2) + int(valg3)
except Exception:
    total_poeng = 0

if total_poeng == 3 or total_poeng == 4:
       print ("Gratulerer! Du har navigert gjennom konfliktene på en effektiv måte, " \
           "og hjulpet teamet med å komme seg gjennom stormingfasen på en godt måte.")
elif total_poeng == 5:
       print ("Teamet sliter fremdeles med tillitsproblemer og konflikter, " \
              "de klarer å fullføre prosjektet, men samarbeidet kunne defintivt vært bedre.")
elif total_poeng == 6:
       print ("Dessverre har teamet ikke klart å håndtere konfliktene på en god måte, " \
              "noe som har ført til at prosjektet har blitt forsinket og kvaliteten på arbeidet, " \
              "har blitt påvirket negativt.")
else:
       print ("Resultatet er uklart, vennligst velg gyldige alternativer for alle konflikter.")

           
#---Slutt---


       
        

    
 
