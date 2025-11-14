
#---------------Erling sine valg---------------

print("\nI storming-fasen oppstår uenighet og usikkerhet når gruppen tester grenser og avklarer roller og mål.", \
      "Konflikter er vanlige, men nødvendige for å skape klarhet og leggegrunnlaget for godt samarbeid videre."
      )

print("\nI starten var stemninga god. Gruppen opplevde høy motivasjon og fellesskap i målet om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. " \
    "Men nå, etter seks uker, har prosjektet til Erling gått inn i den klassiske storming-fasen, der ulike faglige perspektiver og personlige preferanser begynner å kollidere."  )

print("\nDu tar rollen som Erling, og som prosjektleder må du navigere gjennom disse utfordringene for å sikre at prosjektet fortsetter.") 

#--------------- Konflikt 1 ---------------
print("\nDet oppstår en konflikt mellom Silje og Sivert i teamet ditt. Silje (UX-designer) mener at brukeropplevelsen må prioriteres høyest, " \
    "mens Sivert (IT-utvikler) insisterer på at tekniske løsninger må komme først.")

print("\nKonflikten eskalerer, og det begynner å påvirke teamets moral og fremdrift, " \
      "Sakskonflikten har blitt til en personlig konflikt, og de begge drar støtte av andre teammedlemmer.")

print("\nSom prosjektleder må du ta en beslutning om hvordan du skal håndtere denne konflikten.")

print("\nHva gjør du?")

print("1: Arranger et møte med Silje og Sivert for å diskutere konflikten, " \
      "slik at begge parter får uttrykt bekymringene sine og kan finne en felles løsning.")
print("2: Prioriter fremdrift og ta en beslutning på egen hånd uten å involvere dem.")
# variabel for å huske spillerens valg på tvers av konflikter
choices = {}

while True:
    path_choice_1 = input("Velg 1 eller 2 (skriv bare tallet): ")
    if path_choice_1 == "1":
            # lagrer valget slik at senere deler av historien kan få tilgang til det
            choices['conflict1'] = path_choice_1
            print("\nDu arrangerer et møte med Silje og Sivert. Gjennom åpen kommunikasjon og aktiv lytting, " \
                    "klarer dere å finne en felles forståelse og en løsning som begge parter kan akseptere. " \
                    "Teamet føler seg hørt, og samarbeidet forbedres.")
            break
    elif path_choice_1 == "2":
            # lagrer valget slik at senere deler av historien kan få tilgang til det
            choices['conflict1'] = path_choice_1
            print("\nDu velger å prioritere fremdrift og tar en beslutning på egen hånd. " \
                    "Du bestemmer at prosjektet må fokusere på tekniske løsninger først, " \
                    "og kommuniserer dette til teamet uten å involvere Silje og Sivert i prosessen.") 
            print("Dette fører til at Silje føler seg oversett og undervurdert, "
                    "noe som skaper ytterligere spenning i teamet og påvirker moralen negativt.")
            break
    else:
      print("Ugyldig valg. Vennligst velg 1 eller 2.")

#--------------- Konflikt 2 ---------------
print("\nSamtidig som konflikten mellom Silje og Sivert, oppstår det en ny konflikt i teamet ditt. " \
    "Denne gangen er det mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant).")

print("\nHamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform." \
      " mens Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")

print("\nForeløpig er uenigheten lavmælt, men du merker at frustrasjonen vokser.")

print("\nProsjektet nærmer seg en viktig milepæl: første prototype skal være klar om tre uker. " \
    "Stemningen er spent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan, " \
    "avgjøre om teamet beveger seg videre mot 'norming', eller blir stående fast i stormen.")

print("\nHva gjør du?")
print("1: Arranger en workshop med både Hamdi og Jabir, " \
      "slik at de kan diskutere sine perspektiver og finne en felles vei fremover.")
print("2: Velg å avvente situasjonen og håpe at de finner ut av det selv uten din inngripen.")

while True:
    path_choice_2 = input("Velg 1 eller 2 (skriv bare tallet): ")
    if path_choice_2 == "1":
            # lagrer valget slik at senere deler av historien kan få tilgang til det
            choices['conflict2'] = path_choice_2
            print("\nDu arrangerer en workshop med Hamdi og Jabir. Gjennom strukturert dialog og fasilitering, " \
                    "klarer de å forstå hverandres perspektiver bedre og finne en kompromissløsning som ivaretar begge deres behov. " \
                    "Dette styrker teamets samarbeid og fremmer en mer positiv arbeidskultur.")
            break
    elif path_choice_2 == "2":
            # lagrer valget slik at senere deler av historien kan få tilgang til det
            choices['conflict2'] = path_choice_2
            print("\nDu velger å avvente situasjonen og håper at Hamdi og Jabir finner ut av det selv. "\
                    "Dessverre eskalerer konflikten, og deres uenigheter begynner å påvirke teamets dynamikk negativt. "\
                    "Dette fører til redusert samarbeid og økt frustrasjon blant teammedlemmene.")
            break
    else:
      print("Ugyldig valg. Vennligst velg 1 eller 2.")

#--------------- Konflikt 3 ---------------

print("\nMed bare tre uker igjen til første prototype skal leveres, merker du at teamets motivasjon og fokus begynner å vakle. " \
    "Den pågående konflikten mellom Silje og Sivert, samt Hamdi og Jabir, har skapt en anspent atmosfære.")
print("\nSom prosjektleder må du ta grep for å bevare teamets moral og sikre fremdrift mot milepælen.")
print("\nHva gjør du?")
print("1: Arranger en kort teambyggingsaktivitet for å styrke tilliten i teamet, " \
      "samtidig som du legger en klar og realistisk plan for de neste tre ukene.")
print("2: Fokuser på å stramme opp oppfølgingen og fremdriften, " \
      "med hyppige statusmøter og klare leveransemål.")

while True:
    path_choice_3 = input("Velg 1 eller 2 (skriv bare tallet): ")
    if path_choice_3 == "1":
            # lagrer valget slik at senere deler av historien kan få tilgang til det
            choices['conflict3'] = path_choice_3
            print("\nDu arrangerer en kort teambyggingsaktivitet som hjelper teamet med å gjenopprette tilliten og samarbeidet. "\
                    "Samtidig legger du en klar og realistisk plan for de neste tre ukene, "\
                    "som gir teamet en tydelig retning og mål å jobbe mot. "\
                    "Dette fører til økt motivasjon og fokus, og teamet jobber effektivt mot milepælen.")
            break
    elif path_choice_3 == "2":
            # lagrer valget slik at senere deler av historien kan få tilgang til det
            choices['conflict3'] = path_choice_3
            print("\nDu fokuserer på å stramme opp oppfølgingen og fremdriften, "\
                    "med hyppige statusmøter og klare leveransemål. "\
                    "Dette skaper et presset arbeidsmiljø, og teamets motivasjon synker ytterligere. "\
                    "Konfliktene i teamet forverres, og samarbeidet blir stadig mer utfordrende.")
            break
    else:
        print("Ugyldig valg. Vennligst velg 1 eller 2.")

#--------------- Sluttutfall ---------------

# Skriv ut hvilke valg spilleren gjorde (AI)
print("\nDine valg underveis:")
print(f"Konflikt 1: {choices.get('conflict1', 'ingen valg')}")
print(f"Konflikt 2: {choices.get('conflict2', 'ingen valg')}")
print(f"Konflikt 3: {choices.get('conflict3', 'ingen valg')}")

# Bestem slutt basert på en enkel poengberegning:
# Gi hver '1' ett poeng (antatt konstruktivt samarbeid), hver '2' gir 0 poeng.
score = 0
for k in ('conflict1', 'conflict2', 'conflict3'):
        if choices.get(k) == '1':
                score += 1

# Velg en av tre slutninger basert på score
if score == 3:
        ending = 'Bra sluttresultat: Teamet løser konfliktene, leverer prototypen og prosjektet får stor framgang.'
elif score == 2:
        ending = 'Helt ok sluttresultat: Teamet leverer, men noen spenninger forblir. Resultatet er akseptabelt.'
else:
        ending = 'Dårlig sluttresultat: Konfliktene svekker prosjektet og leveransen lider. Flere teammedlemmer vurderer å slutte.'

print('\n--- Slutt ---')
print(ending)

print("Takk for at du simulerte Erlings valg!")
