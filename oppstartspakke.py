# Innleveringsoppgave 2 - Eldar


print("="*60)
print("ERLINGS UTFORDRING: STORMEN")
print("="*60)
print()

# Bakgrunnsinformasjon
print("Bakgrunnsinformasjon:")
print()
print("Erling er prosjektleder for kommunens utvikling av medborger-portal.")
print("Teamet består av:")
print()
print("- Sivert: IT-rådgiver, opptatt av teknisk sikkerhet og kostnadskontroll")
print("- Silje: UX/UI-designer, fokusert på brukervennlighet og innovasjon")
print("- Hamdi: Kulturavdeling, ansvarlig for innbygger-dialog")
print("- Jabir: Brukerrepresentant fra lokal innbygger-forening")
print()
print("Starten var som alle andre prosjekter, fylt av pågangsmot og stå-på-vilje,")
print("men etterhvert som tiden gikk, passerte også norming-fasen og nå, etter")
print("6 uker, så Erling at stormen var på veg. Både billedlig og bokstavelig ment.")
print()
input("Trykk ENTER for å starte historien...")
print()

# Variabler for å tracke valg
poeng_kapittel1 = 0
poeng_kapittel2 = 0
poeng_kapittel3 = 0

# KAPITTEL 1: Konflikten mellom Sivert og Silje
print("="*60)
print("KAPITTEL 1: TEKNOLOGI VS. DESIGN")
print("="*60)
print()
print("Den første konflikten som melder sitt anbud er mellom Sivert og Silje.")
print()
print("Sivert er ikke enig i Silje sine avgjørelser angående design og valg av")
print("teknologi. Han mener forslaget er for urealistisk, usikkert og kostbart.")
print()
print("Silje forsvarer sine valg etter beste evne og påpeker at Sivert sine")
print("forslag vil låse brukeropplevelsen og hindre innovasjon.")
print()
print("Aiai, dette er ikke greit. Dette har nå nådd punktet der det ikke lenger")
print("gjelder sak, men er nå personangrep.")
print()
print("Hva skal Erling gjøre nå?")
print()
print("1. Arrangere et konstruktivt møte hvor begge får legge frem sine")
print("   argumenter, og sammen finne en kompromissløsning som balanserer")
print("   innovasjon og realisme.")
print()
print("2. Ta en rask beslutning basert på budsjett og tid - velge Siverts")
print("   konservative løsning uten videre diskusjon.")
print()

valg1 = input("Hva velger Erling? (1/2): ")

if valg1 == "1":
    print()
    print("Erling velger å arrangere et fasilitert møte hvor både Sivert og Silje")
    print("får presentere sine synspunkter. Etter grundig diskusjon finner de en")
    print("mellomløsning: De bruker etablert teknologi som grunnmur, men med")
    print("fleksibilitet for framtidig innovasjon.")
    print()
    print("Både Sivert og Silje føler seg hørt. Teamet puster lettet ut.")
    print("Dette var den gode løsningen - alle parter er fornøyde.")
    poeng_kapittel1 = 2
    print()
elif valg1 == "2":
    print()
    print("Erling velger å ta en rask beslutning og går for Siverts løsning.")
    print("Konflikten stoppes umiddelbart, men Silje føler seg overkjørt.")
    print("Hun blir stille og mindre engasjert i prosjektet.")
    print()
    print("Dette var den mindre optimale løsningen - flere er misfornøyde,")
    print("men problemet er løst.")
    poeng_kapittel1 = 1
    print()
else:
    print()
    print("Ugyldig valg! Erling unnviker konflikten og lar den ulme videre.")
    print("Sivert og Silje slutter å snakke sammen. Prosjektet lider.")
    poeng_kapittel1 = 0
    print()

input("Trykk ENTER for å fortsette...")
print()

# KAPITTEL 2: Konflikten mellom Jabir og Hamdi
print("="*60)
print("KAPITTEL 2: DIGITALE FOLKEMØTER")
print("="*60)
print()
print("I periferien av synet har nå den ulmende konflikten mellom")
print("Jabir og Hamdi eskalert og nærmer seg nå bristepunktet.")
print()
print("De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter.")
print()
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende")
print("plattform og er veldig bastant på dette, mens Jabir ønsker et mer åpent,")
print("dialogbasert system med rom for spontane innspill.")
print()
print("Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser.")
print()
print("Prosjektet nærmer seg en viktig milepæl: første prototype skal være klar")
print("om tre uker. Stemningen er spent, kommunikasjonen hakkete, og Erling vet")
print("at hans neste valg kan avgjøre om teamet beveger seg videre mot 'norming'")
print("– eller blir stående fast i stormen.")
print()
print("1. Sette av tid til en workshop hvor Jabir og Hamdi sammen med")
print("   sluttbrukere kan teste begge løsninger og la data avgjøre.")
print()
print("2. Velge Hamdis løsning fordi den er tryggere og raskere å")
print("   implementere, selv om Jabir blir misfornøyd.")
print()

valg2 = input("Hva velger Erling? (1/2): ")

if valg2 == "1":
    print()
    print("Erling velger å organisere en workshop med innbyggere fra målgruppen.")
    print("Både Jabirs og Hamdis løsninger blir testet. Resultatene viser at")
    print("en hybrid-løsning fungerer best: Hamdis sikre plattform som base,")
    print("med Jabirs dialogfunksjoner som tillegg.")
    print()
    print("Jabir og Hamdi er begge fornøyde med kompromisset.")
    print("Dette var den gode løsningen.")
    poeng_kapittel2 = 2
    print()
elif valg2 == "2":
    print()
    print("Erling velger Hamdis løsning på grunn av tidspress og sikkerhet.")
    print("Hamdi nikker fornøyd, men Jabir blir stille og frustrert.")
    print()
    print("'Jeg føler ikke at mine ideer blir hørt,' sier Jabir.")
    print("Dette var den dårlige løsningen.")
    poeng_kapittel2 = 0
    print()
else:
    print()
    print("Ugyldig valg! Erling ber dem 'finne ut av det selv'.")
    print("Konflikten eskalerer og påvirker resten av teamet negativt.")
    poeng_kapittel2 = 0
    print()

input("Trykk ENTER for å fortsette...")
print()

# KAPITTEL 3: Motivasjon og teambygging
print("="*60)
print("KAPITTEL 3: VEIEN MOT PROTOTYPEN")
print("="*60)
print()

if poeng_kapittel1 + poeng_kapittel2 >= 3:
    print("Etter de to konfliktene er stemninga i teamet relativt positiv.")
    print("Erling har håndtert utfordringene godt.")
elif poeng_kapittel1 + poeng_kapittel2 >= 2:
    print("Stemningen i teamet er blandet. Noen er fornøyde, andre føler seg")
    print("oversett. Det er litt anspent.")
else:
    print("Stemningen i teamet er anstrengt. Kommunikasjonen er dårlig,")
    print("flere føler seg overkjørt, og motivasjonen er lav.")

print()
print("Erling lurer på hva han kan gjøre for å lette på trykket/motivere")
print("teamet videre mot prototypen som skal være klar om tre uker.")
print()
print("1. Arrangere en teambuilding-aktivitet og en ærlig samtale om")
print("   hva som fungerer og hva som må forbedres. Vise at du bryr deg")
print("   om teamet som mennesker, ikke bare som ressurser.")
print()
print("2. Fokusere fullt på arbeid, øke tempoet og presse på for å nå")
print("   milepælen - motivere med å fullføre oppgaven.")
print()

valg3 = input("Hva velger Erling? (1/2): ")

if valg3 == "1":
    print()
    print("Erling velger å ta teamet med på en sosial aktivitet og setter av tid")
    print("til en retrospektiv hvor alle får dele sine tanker åpent.")
    print()
    print("Silje takker Erling for at han lytter. Sivert nikker anerkjennende.")
    print("Jabir og Hamdi ler sammen og finner felles grunn.")
    print()
    print("Teamet føler seg sett og hørt. Motivasjonen øker.")
    poeng_kapittel3 = 2
    print()
elif valg3 == "2":
    print()
    print("Erling velger å presse på med arbeidet. 'Vi må levere!' sier han.")
    print()
    print("Noen i teamet setter pris på fokuset, men andre blir utslitte.")
    print("Silje sukker og jobber overtid uten entusiasme.")
    print()
    print("Prototypen blir ferdig i tide, men til en kostnad for teamet.")
    poeng_kapittel3 = 1
    print()
else:
    print()
    print("Ugyldig valg! Erling gjør ingenting ekstra.")
    print("Teamet føler seg neglisjert og motivasjonen synker ytterligere.")
    poeng_kapittel3 = 0
    print()

input("Trykk ENTER for å se avslutningen...")
print()

# AVSLUTNING basert på sum av valg
total_poeng = poeng_kapittel1 + poeng_kapittel2 + poeng_kapittel3

print("="*60)
print("AVSLUTNING")
print("="*60)
print()

if total_poeng >= 5:
    # Avslutning 1: Positiv
    print("🌟 FANTASTISK RESULTAT! 🌟")
    print()
    print("Alt blir gjort på tiden og teamet er positivt innstilt!")
    print()
    print("Prototypen blir ferdig akkurat til tidsfristen, og kvaliteten er")
    print("utmerket. Teamet har utviklet et sterkt samhold gjennom alle")
    print("utfordringene de har løst sammen.")
    print()
    print("Silje og Sivert jobber nå som et godt team, med gjensidig respekt.")
    print("Jabir og Hamdi har lært av hverandres perspektiver og utviklet")
    print("en innovativ hybrid-løsning.")
    print()
    print("Kommunen er svært fornøyd. Prosjektet blir sett på som en")
    print("referanse for hvordan man driver gode digitaliseringsprosjekter.")
    print()
    print("Erling har vist at god ledelse handler om å:")
    print("✓ Håndtere konflikter konstruktivt")
    print("✓ La teamet være med på beslutninger")
    print("✓ Bry seg om mennesker, ikke bare oppgaver")
    print()
elif total_poeng >= 3:
    # Avslutning 2: Middels
    print("😐 MIDDELS RESULTAT")
    print()
    print("Prosjektet blir såvidt gjennomført på tiden og det er")
    print("lunken stemning i teamet.")
    print()
    print("Prototypen fungerer og leveres i tide, men entusiasmen er dempet.")
    print("Noen i teamet er fornøyde, andre føler at deres perspektiver")
    print("ikke ble tatt nok på alvor.")
    print()
    print("Silje og Sivert snakker sammen, men det er fortsatt en viss distanse.")
    print("Jabir er usikker på om hans innspill virkelig ble verdsatt.")
    print()
    print("Kommunen aksepterer resultatet, men hadde forventet mer.")
    print("Det er rom for forbedring i både produkt og prosess.")
    print()
    print("Erling lærer at kompromisser er nødvendige, men at han kunne")
    print("håndtert konflikter bedre og involvert teamet mer i beslutninger.")
    print()
else:
    # Avslutning 3: Dårlig
    print("😞 UTFORDRENDE RESULTAT")
    print()
    print("Prosjektet er dårlig gjennomført. Folk skaffer sykemelding for å")
    print("ikke jobbe sammen. Kontrakten blir terminert og prosjektet ble ikke")
    print("ferdigstilt før 1 måned etter tidsfristen.")
    print()
    print("Stemningen i teamet er giftig. Silje søker seg til et annet prosjekt.")
    print("Sivert jobber alene og kommuniserer minimalt. Jabir og Hamdi snakker")
    print("knapt sammen.")
    print()
    print("Kommunen er sterkt misfornøyd. Prosjektet blir trukket frem som et")
    print("eksempel på hvordan man IKKE skal drive digitaliseringsprosjekter.")
    print()
    print("Erling lærer den harde veien at ledelse krever:")
    print("✗ Aktivt konfliktløsning, ikke unnvikelse")
    print("✗ Å lytte til teamet og involvere dem i beslutninger")
    print("✗ Å balansere leveranse med teamets velvære")
    print()
    print("Dette var en lærerik, men smertefull opplevelse.")
    print()

print("="*60)
print(f"Din totale score: {total_poeng}/6")
print("="*60)
print()
print("Takk for at du spilte!")
print("="*60)
