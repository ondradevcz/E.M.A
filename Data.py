# zakladni tasky
ai_output = ""

t_help_task = ("help", "Help", "Pomoc", "pomoc")

t_help_guide = ("\n Napiš příslušné číslo či název operace pro Start." 
                "\n\n 1. Výpočet Výživného - vypočti si přibližnou výši výživného nějaké danné osoby." 
                "\n 2. Výpočet Věku - vypočti si kolik někomu je podle toho kdy se narodil." 
                "\n 3. Tipy jak zefektivnit práci - zjisti jak si zefektivnit práci." 
                "\n 4. Připomínky - můžeš vytvářet nebo mazat poznámky."
                "\n 5. Password Generátor - vygeneruj si svoje nové bezpečné heslo."
                "\n 6. BMI Calculator - vypočti si svoji hodnotu BMI."
                "\n 7. Simple Timer - spustíš časovač a ten běží do nekonečna."
                "\n 8. Rock Paper Scissors - můžeš si se mnou zahrát kámen, nůžky, papír, teď."
                "\n 9. Chuck Norris vtipy - nech si povědět vtip o známém herci a mistrovi bojových umění." 
                "\n 10. Diktafon - nadiktuj text a Ema ti ho vypíše."
)

t_konec = ("Konec", "konec", "end", "End", "Ending", "ending")

t_data_na_ktere_nedokazal_odpovedet = []

# judge.ai funkce
t_výpočet_výživného = ('1', '1.', 'Výpočet Výživného',
                              'výpočet výživného', 'Výpočet výživného')

t_výpočet_věku = ('2', '2.', 'Výpočet Věku', 'Výpočet věku',
                         'výpočet věku')

t_tipy_jak_zefektivnit_práci_reakce = ('3', '3.', 'Tipy jak zefektivnit práci')

t_todolist = ("4", "4.", "To-do List", "todo list", "to-do list", "To-do list", "Todo list", "připomínky", "Připomínky")

t_tipy_jak_zefektivnit_práci = (
    '\n1. Organizace a plánování:\n\n Vytvořte si denní a týdenní plán práce, případně si nechte prostor na předběžná opatrění kdyby z ničeho nic přišly.\n\n Priorizujte případy podle jejich naléhavosti a komplexnosti.\n\n Využijte kalendář a plánovač, abyste si zpřehlednili termíny slyšení a lhůty pro rozhodnutí.\n\n Doporučuji klasický Apple či Google kalendář ale jinak jsou tu varianty jako Notion, ten funguje i na hromadu dalších věcí jako je tkz. Second Brain. Jednoduše to je zápisník na všechny nápady co vás napadnou, kdykoli.',
    '\n\n\n2. Zpětná vazba a reflexe:\n\n Pravidelně se ohlížejte za svou prací a přemýšlejte o tom, jak byste mohli být ještě efektivnější.\n\n Přijímejte konstruktivní zpětnou vazbu od kolegů a zaměstnanců.',
    '\n\n\n3. Fyzička:\n\n Bude to znít jako klišé ale fyzička a celková fyzická zdatnost je základ všeho. Pokud máte vysportované tělo tak se budete cítit fyzicky i psychicky lépe, tudíž i to bude mít vliv na efektivnost a rychlost vaší práce. Zároveň každý bude s vámi jednat s větším respektem.'
)


# zakladni data
t_greetings = ("Ahoj", "Čau", "Dobrý den", "Dobrý den", "Dobrý den", "ahoj")

t_ai_greetings = ("Čest práci soudruhu", "Pozdrav pán bůh", "Ahojda", "Dobrý den přeji", "Nazdárek")


# personalizace
t_age = ("starý", "let")

t_zajmeno = ("Já", "Jsem", "Je", "je", "se", "Se")

t_otazka_na_vek = ("kolik", "Kolik")

t_number = tuple(str(i) for i in range(122))

jmeno_zeny_p = None
jmeno_zeny_n = None

t_jmena_žen = (
    'Tereza', 'Barbora', 'Anna', 'Kateřina', 'Lucie', 'Veronika', 'Markéta', 'Adéla', 'Nikola', 'Eliška',
    'Karolína', 'Kristýna', 'Simona', 'Michaela', 'Petra', 'Denisa', 'Klára', 'Gabriela', 'Dominika', 'Alžběta',
    'Jana', 'Natálie', 'Martina', 'Kamila', 'Vendula', 'Šárka', 'Helena', 'Andrea', 'Aneta', 'Viktorie',
    'Marcela', 'Lenka', 'Pavla', 'Ivana', 'Hana', 'Klaudie', 'Zuzana', 'Kristina', 'Nela', 'Klára', 'Diana',
    'Iveta', 'Aneta', 'Romana', 'Žaneta', 'Monika', 'Magdaléna', 'Veronika', 'Laura', 'Julie', 'Eliška', 'Klára',
    'Johana', 'Jitka', 'Ivona', 'Linda', 'Dagmar', 'Štěpánka', 'Patricie', 'Alice', 'Radka', 'Lea', 'Klára',
    'Katarína', 'Anna', 'Helena', 'Daniela', 'Nikola', 'Natálie', 'Nikola', 'Nikola', 'Kristina', 'Klára', 'Karin',
    'Veronika', 'Tereza', 'Barbora', 'Kateřina', 'Lucie', 'Petra', 'Markéta', 'Adéla', 'Eliška', 'Kristýna', 'Anna',
    'Karolína', 'Nikola', 'Simona', 'Veronika', 'Denisa', 'Kateřina', 'Adéla', 'Lucie', 'Anna', 'Tereza', 'Barbora',
    'Klára', 'Kateřina', 'Veronika', 'Eliška', "Beáta"
)

t_pozitivni_zeny = ("Miluju", "rád", "líbí", "miluju", "miluji", "Miluji", "Líbí")

t_negativni_zeny = ("Rozešla", "Rozešel", "rozešla", "rozešel", "podvedl", "Podvedl", "podvedla", "Podvedla")

jmeno_uzivatele = ""

t_convo_jmeno = ("Jmenuji", "jmenuji", "jmenuju", "Jmenuju", "Jméno", "jméno")

t_jmena_muzu = (
    "Adam", "Matěj", "Jan", "Tomáš", "David", "Filip", "Jakub", "Ondřej", "Martin", "Petr",
    "Michal", "Lukáš", "Jiří", "Karel", "Vojtěch", "Daniel", "Štěpán", "Marek", "Dominik", "Erik",
    "Aleš", "Antonín", "Bohumil", "Bohuslav", "Gabriel", "Hugo", "Ivan", "Jaroslav", "Josef", "Ladislav",
    "Leoš", "Libor", "Lubomír", "Luboš", "Milan", "Miloš", "Miroslav", "Pavel", "Richard", "Robert",
    "Rudolf", "Stanislav", "Tomáš", "Václav", "Viktor", "Vladimír", "Vlastimil", "Vojtěch", "Zdeněk",
    "Zbyněk", "Zdenko", "Zoltán", "Žigmund", "Žan", "Želek", "Žaneta"
)

t_convo_otazka = ("Jak", "jak", "?", "Jaký", "jaký")

t_pozitivni_nalada = ("Dobře", "Výborně", "Parádně", "dobře", "výborně", "parádně")

t_negativni_nalada = ("Špatně", "Hrozně", "Nanic", "špatně", "hrozně", "nanic")


# sentence indexing

index_predchozi_vety = None
# například jak_se_mas

types_of_indexes = ("jak_se_mas", ) # jen pro informaci

t_ano = ("Ano", "ano", "jo", "Jo", "Yes", "yes", "jde", "Jde")

t_ne = ("Ne", "ne", "Nejde", "nejde")

t_passwordgenerator = ("passwordgenerator", "Passwordgenerator", "PasswordGenerator", "Password Generator", "password generator", "Passwordgenerator", "5", "5.")

t_bmicalculator = ("bmicalculator, bmi calculator", "BMI Calculator", "bmi Calculator,", "BMI calculator", "6", "6.")

t_simpletimer = ("timer", "Timer", "SimpleTimer", "simpletimer", "Simpletimer", "Simple Timer", "Simple timer", "7", "7.")

t_rockpaperscissors = ("RockPaperScissors", "Rock Paper Scissors", "rock paper scissors", "rpc", "RPC", "8", "8.")

t_den = ("Den", "den")

t_dnes = ("Dnes", "dnes", "dneska", "Dneska")

t_vanoce = ("Vánoce", "vánoce")

t_novy_rok = ("Nový rok", "nový rok")

t_jak_je = ("Jak je", "jak je", "Jak se vede", "jak se vede", "jak se máš", "Jak se máš")

t_vtipy = ("vtip", "vtipy", "Vtipy", "Vtip")

t_chuck_norris = ("Chuck", "Norris", "chuck", "norris", "chuckovi", "Chuckovi", "Norrisovi", "norrisovi", "chucku", "Chucku", "9", "9.")

t_chuck_norris_vtipy = ("Když Alexander Bell vynalezl telefon, měl na něm tři zmeškané hovory od Chucka Norrise.", 
                        "Strachu z pavouků se říká arachnofobie, strachu z malých prostorů klaustrofobie a strachu z Chucka Norrise logické myšlení.",
                        "Chuck Norris byl na Marsu. Proto tam nejsou žádné známky života.",
                        "Chuck Norris má doma koberec z grizzlyho. Grizzly není mrtvý, jen se bojí pohnout.",
                        "Chuck Norris umí zabouchnout otáčivé dveře.",
                        "Chuck Norris hrál kámen, nůžky, papír se zrcadlem a vyhrál.",
                        "Chuck Norris nenosí hodinky. On rozhoduje, kolik je hodin!",
                        "Evoluční teorie je hloupost. Existuje pouze seznam zvířat, kterým Chuck Norris dovolil žít.",
                        "Chuck Norris nečte knihy. Zírá na ně tak dlouho, až mu řeknou všechno, co chce vědět.",
                        "Vesmír je kolem Země jenom proto, že se bojí bejt na stejný planetě s Chuckem Norrisem.",
                        "Pokud zahrajete ve scrabble „Chuck Norris“, vyhráli jste. Navždycky.",
                        "Když jde Chuck Norris přes ulici, auta se musí rozhlídnout na obě strany.")

t_diktofon = ("diktafon", "Diktafon", "10", "10.", "Diktovat", "diktovat")

t_podekovani = ("děkuji", "Děkuji", "Děkuju", "děkuju", "dík", "Dík", "díky", "Díky")
