from datetime import date
import datetime
from Data import *
import random
from tinydb import TinyDB, Query
db = TinyDB('db3.json')
import time
import speech_recognition as sr
import elevenlabs

User = Query()

# CHATBOT -------------------------------------------------------------

class Chatbot():

  def __init__(self):

    # Tasks -----------------------------------------------------------
    self.l_data_na_ktere_nedokazal_odpovedet = t_data_na_ktere_nedokazal_odpovedet
    self.index_predchozi_vety = index_predchozi_vety
    self.recognizer = sr.Recognizer()
    self.general_input = ""
    self.ai_output = ai_output

  def GeneralInput(self):

    def listen_and_recognize(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                return

        try:
            print("Recognizing...")
            self.general_input = self.recognizer.recognize_google(audio, language="cs-CZ")
            print("You said: " + self.general_input)
            # Process the recognized text here

        except sr.UnknownValueError:
            print("Nerozumím, zkus to znova")
            self.GeneralInput()
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    self.general_input_split = self.general_input.split() # Pouzivat jen pokud budu potrebat s for loopem vyhledat a ulozit slova v te vete(self):

    self.recognizer = sr.Recognizer()
    self.general_input = ""

    listen_and_recognize(self)

    def GenerateAudio(self):
      audio = elevenlabs.generate(
      api_key="638ad62e835c089bf5039d122cf0e843",
      text=self.ai_output,
      voice="Rachel",
      model="eleven_multilingual_v2"
      )

      elevenlabs.play(audio)

    if any(ending in self.general_input for ending in t_konec):
      self.ai_output = "Děkuji za konverzaci, měj se."
      GenerateAudio(self)
      self.ai_output = (f"Pro debug, zde jsou data na které AI nedokázalo odpovědět: {self.l_data_na_ktere_nedokazal_odpovedet}")
      print(f"Pro debug, zde jsou data na které AI nedokázalo odpovědět: {self.l_data_na_ktere_nedokazal_odpovedet}")
      GenerateAudio(self)

    elif any(greeting in self.general_input for greeting in t_greetings):
        self.ai_output = random.choice(t_ai_greetings)
        GenerateAudio(self)
        time.sleep(3)
        self.GeneralInput()

    elif any(test in self.general_input for test in t_zajmeno) and any(test in self.general_input for test in t_age) and any(test in self.general_input for test in t_number):
        if db.search(User.age.exists()):
          věk_uživatele = next(filter(str.isdigit, self.general_input.split()), None)
          věk_uživatele = int(věk_uživatele)
          db.update({"age": věk_uživatele}, User.age.exists())
          self.ai_output = "Dobře"
          GenerateAudio(self)
        else:
          věk_uživatele = next(filter(str.isdigit, self.general_input.split()), None)
          věk_uživatele = int(věk_uživatele)  
          db.insert({"age": věk_uživatele})
        self.GeneralInput()

    elif any(test in self.general_input for test in t_otazka_na_vek) and any(test in self.general_input for test in t_zajmeno) and any(test in self.general_input for test in t_age):
        db_age = db.search((User.age.exists()))
        if db_age:
            query_user_age = db_age[0]['age']
            self.ai_output = f"Je ti {query_user_age} let."
            GenerateAudio(self)
            print(f"Je ti {query_user_age} let.")
            self.GeneralInput()
        else:
            print("Nevím kolik ti je.")
            self.ai_output = "Nevím kolik ti je let"
            GenerateAudio(self)
            self.GeneralInput()

    elif any(help in self.general_input for help in t_help_task):
      self.ai_output = t_help_guide
      GenerateAudio(self)
      print(t_help_guide)
      self.GeneralInput()

    elif any(výpočet_výživného in self.general_input for výpočet_výživného in t_výpočet_výživného):
      self.StartVýpočetVýživného()

    elif any(výpočet_věku in self.general_input for výpočet_věku in t_výpočet_věku):
      VýpočetVěku()

    elif any(tipy_jak_zefektivnit_práci in self.general_input for tipy_jak_zefektivnit_práci in t_tipy_jak_zefektivnit_práci_reakce):
      for element in t_tipy_jak_zefektivnit_práci:
        self.ai_output = element
        GenerateAudio(self)
        print(element)
      self.GeneralInput()

    elif any(vesele_vanoce in self.general_input for vesele_vanoce in t_vanoce):
      print("Veselé vánoce")
      self.ai_output = "Přeji vám všem Veselé Vánoce"
      GenerateAudio(self)
      self.GeneralInput()

    elif any(stastny_novy_rok in self.general_input for stastny_novy_rok in t_novy_rok):
      print("Šťastný Nový rok")
      self.ai_output = "Přeji vám všem Šťastný Nový Rok"
      GenerateAudio(self)
      self.GeneralInput()

    elif any(zeny in self.general_input for zeny in t_pozitivni_zeny):
      if any(zeny in self.general_input for zeny in t_jmena_žen):
        print(self.general_input_split)
        for slovo in self.general_input_split:
            if slovo in t_jmena_žen:
              jmeno_zeny_p = slovo
              break
              
        if jmeno_zeny_p:
            if db.search(User.zena_pozitivni.exists()):
              db.update({"zena_pozitivni": jmeno_zeny_p}, User.zena_pozitivni.exists())
              print(jmeno_zeny_p)
            else:
              print(f"Jméno {jmeno_zeny_p} bylo nalezeno a uloženo do databáze.")
              db.insert({"zena_pozitivni": jmeno_zeny_p})
            self.GeneralInput()
        else:
            print("Žádné jméno nebylo nalezeno v zadané větě.")
            self.GeneralInput()
      elif db.search(User.zena_pozitivni.exists()):
        db_zena_pozitivni = db.search((User.zena_pozitivni.exists()))
        if db_zena_pozitivni:
          query_user_zena_pozitivni = db_zena_pozitivni[0]['zena_pozitivni']
          print(f"Líbí se ti {query_user_zena_pozitivni}.")
          self.GeneralInput()
      else:
        print("Nevím kdo se ti líbí.")
        self.GeneralInput()

    elif any(zeny in self.general_input for zeny in t_negativni_zeny):
      if any(zeny in self.general_input for zeny in t_jmena_žen):
        print(self.general_input_split)
        for slovo in self.general_input_split:
            if slovo in t_jmena_žen:
              jmeno_zeny_n = slovo
              break
              
        if jmeno_zeny_n:
            if db.search(User.zena_negativni.exists()):
              db.update({"zena_pozitivni": jmeno_zeny_n}, User.zena_negativni.exists())
              print(jmeno_zeny_n)
            else:
              print(f"Jméno {jmeno_zeny_n} bylo nalezeno a uloženo do databáze.")
              db.insert({"zena_negativni": jmeno_zeny_n})
            self.GeneralInput()
        else:
            print("Žádné jméno nebylo nalezeno v zadané větě.")
            self.GeneralInput()
      elif db.search(User.zena_negativni.exists()):
        db_zena_negativni = db.search((User.zena_negativni.exists()))
        if db_zena_negativni:
          query_user_zena_negativni = db_zena_negativni[0]['zena_negativni']
          print(f"Podvedla tě {query_user_zena_negativni}.")
          self.GeneralInput()
      else:
          print("Nevím kdo tě podvedl.")
          self.GeneralInput()
    
    elif any(otazka_na_jmeno_uzivatele in self.general_input for otazka_na_jmeno_uzivatele in t_convo_otazka) and any(otazka_na_jmeno_uzivatele in self.general_input for otazka_na_jmeno_uzivatele in t_convo_jmeno):
      db_jmeno_uzivatele = db.search((User.jmeno_uzivatele.exists()))
      if db_jmeno_uzivatele:
        query_jmeno_uzivatele = db_jmeno_uzivatele[0]['jmeno_uzivatele']
        print(f"Jmenuješ se {query_jmeno_uzivatele}.")
        self.ai_output = f"Jmenuješ se {query_jmeno_uzivatele}."
        GenerateAudio(self)
        self.GeneralInput()
      else:
        print("Nevím jak se jmenuješ.")
        self.ai_output = "Nevím jak se jmenuješ."
        GenerateAudio(self)
        self.GeneralInput()

    elif any(jmeno in self.general_input for jmeno in t_convo_jmeno) and any(jmeno in self.general_input for jmeno in t_zajmeno):
      if any(jmeno in self.general_input for jmeno in t_jmena_žen) or any(jmeno in self.general_input for jmeno in t_jmena_muzu):
        print(self.general_input_split)
        for slovo in self.general_input_split:
            if slovo in t_jmena_žen or slovo in t_jmena_muzu:
              jmeno_uzivatele = slovo
              break
        
        if jmeno_uzivatele:
            if db.search(User.jmeno_uzivatele.exists()):
              self.ai_output = "Jméno uživatele bylo aktualizováno."
              db.update({"jmeno_uzivatele": jmeno_uzivatele}, User.jmeno_uzivatele.exists())
              if jmeno_uzivatele in t_jmena_muzu:
                osloveni_jmeno_uzivatele = jmeno_uzivatele + "i"
                db.update({"osloveni_jmeno_uzivatele": osloveni_jmeno_uzivatele})
              elif jmeno_uzivatele in t_jmena_žen:
                osloveni_jmeno_uzivatele = jmeno_uzivatele + "o"
                db.update({"osloveni_jmeno_uzivatele": osloveni_jmeno_uzivatele})
              print(jmeno_uzivatele)
            else:
              print(f"Jméno {jmeno_uzivatele} bylo nalezeno a uloženo do databáze.")
              self.ai_output = f"Jméno {jmeno_uzivatele} bylo nalezeno a uloženo do databáze."
              GenerateAudio()
              db.insert({"jmeno_uzivatele": jmeno_uzivatele})
              if jmeno_uzivatele in t_jmena_muzu:
                osloveni_jmeno_uzivatele = jmeno_uzivatele + "i"
                db.insert({"osloveni_jmeno_uzivatele": osloveni_jmeno_uzivatele})
              elif jmeno_uzivatele in t_jmena_žen:
                osloveni_jmeno_uzivatele = jmeno_uzivatele + "o"
                db.insert({"osloveni_jmeno_uzivatele": osloveni_jmeno_uzivatele})
            self.GeneralInput()

    elif (self.index_predchozi_vety == "jak_se_mas") and any(nalada in self.general_input for nalada in t_pozitivni_nalada):
      self.ai_output = "To ráda slyším."
      GenerateAudio(self)
      print("To ráda slyším")
      self.index_predchozi_vety = None
      self.GeneralInput()

    elif (self.index_predchozi_vety == "jak_se_mas") and any(nalada in self.general_input for nalada in t_negativni_nalada):
      self.ai_output = "To mě mrzí, co se stalo?"
      GenerateAudio(self)
      print("To mě mrzí, co se stalo?")
      self.index_predchozi_vety = "negativni_nalada"
      self.GeneralInput()

    elif self.index_predchozi_vety == "negativni_nalada":
      self.ai_output = "A můžeš s tím něco dělat?"
      GenerateAudio(self)
      print("A můžeš s tím něco dělat?")
      self.index_predchozi_vety = "odpoved_na_duvod_negativni_nalady"
      self.GeneralInput()

    elif (self.index_predchozi_vety == "odpoved_na_duvod_negativni_nalady") and any(odpoved in self.general_input for odpoved in t_ne):
      self.ai_output = "Tak se tím netrap. Samozřejmě je jednoduché říct ať se tím netrápiš ale jak to dopadne ukáže čas. Něco ti povím."
      GenerateAudio(self)
      print("Tak se tím netrap. Samozřejmě je jednoduché říct ať se tím netrápiš ale jak to dopadne ukáže čas. Něco ti povím.")
      self.ai_output = "Jedno přísloví říká: Včerejšek je historie, zítřek je tajemství, ale dnešek je dar."
      GenerateAudio(self)
      time.sleep(2)
      print("Jedno přísloví říká: Včerejšek je historie, zítřek je tajemství, ale dnešek je dar.")
      self.index_predchozi_vety = None
      self.GeneralInput()

    elif (self.index_predchozi_vety == "odpoved_na_duvod_negativni_nalady") and any(odpoved in self.general_input for odpoved in t_ano):
      self.ai_output = "Tak si v klidu rozmysli co s tím chceš dělat a konej."
      GenerateAudio(self)
      print("Tak si v klidu rozmysli co s tím chceš dělat a konej.")
      self.index_predchozi_vety = None
      self.GeneralInput()

    elif any(todolist in self.general_input for todolist in t_todolist):
      from Funkce import Launch_ToDoListApp
      Launch_ToDoListApp()

    elif any(passwordgenerator in self.general_input for passwordgenerator in t_passwordgenerator):
      from Funkce import PasswordGenerator
      PasswordGenerator()

    elif any(bmicalculator in self.general_input for bmicalculator in t_bmicalculator):
      from Funkce import BMI_Calculator
      BMI_Calculator()

    elif any(simpletimer in self.general_input for simpletimer in t_simpletimer):
      from Funkce import SimpleTimer
      SimpleTimer()

    elif any(rockpaperscissors in self.general_input for rockpaperscissors in t_rockpaperscissors):
      from Funkce import RockPaperScissors
      RockPaperScissors()

    elif any(dnesnidatum in self.general_input for dnesnidatum in t_convo_otazka) and any(dnesnidatum in self.general_input for dnesnidatum in t_dnes) and any(dnesnidatum in self.general_input for dnesnidatum in t_den):

      current_date = datetime.datetime.now()
      formatted_date = current_date.strftime("%Y-%m-%d (%A)")
      print(f"Dnes je {formatted_date}")

    elif any(ai_nalada in self.general_input for ai_nalada in t_jak_je):
      self.ai_output = f"Děkuju že se ptáš, mám se {random.choice(t_pozitivni_nalada)}"
      GenerateAudio(self)
      print(f"Děkuju že se ptáš, mám se {random.choice(t_pozitivni_nalada)}")
      self.GeneralInput()

    elif any(chuck_vtip in self.general_input for chuck_vtip in t_vtipy) and any(chuck_vtip in self.general_input for chuck_vtip in t_chuck_norris):
      chuck_norris_vtip = random.choice(t_chuck_norris_vtipy)
      self.ai_output = chuck_norris_vtip
      GenerateAudio(self)
      print(chuck_norris_vtip)
      time.sleep(3)
      self.GeneralInput()

    elif any(podekovani in self.general_input for podekovani in t_podekovani):
      print("Není zač")
      self.ai_output = "Není zač"
      GenerateAudio(self)
      self.GeneralInput()

    else:
      print("Nerozumím, zkus to znova")
      self.ai_output = "Nerozumím, zkus to znova"
      GenerateAudio(self)
      self.GeneralInput()


    # START FUNCTION
      
  def Start(self):

    def GenerateAudio(self):
      audio = elevenlabs.generate(
      api_key="638ad62e835c089bf5039d122cf0e843",
      text=self.ai_output,
      voice="Rachel",
      model="eleven_multilingual_v2"
      )
      elevenlabs.play(audio)

    print(
        '\nAhoj, moje jméno je E.M.A. (Essential Multifunctional Assistant), napiš "/help" a tak zjistíš všechny moje funkce.'
    )
    time.sleep(1)
    db_osloveni_jmeno_uzivatele = db.search((User.osloveni_jmeno_uzivatele.exists()))
    if db_osloveni_jmeno_uzivatele:
      query_osloveni_jmeno_uzivatele = db_osloveni_jmeno_uzivatele[0]['osloveni_jmeno_uzivatele']
      print(f"\nJak se dneska máš {query_osloveni_jmeno_uzivatele}?")
      self.ai_output = f"Ahoj! Jak se dneska máš {query_osloveni_jmeno_uzivatele}?"
      GenerateAudio(self)
      self.index_predchozi_vety = "jak_se_mas"
      print(self.index_predchozi_vety)
    else:
      print("\nJak se jmenuješ?")
    self.GeneralInput()

  def GenerateAudio(self):
      audio = elevenlabs.generate(
      api_key="638ad62e835c089bf5039d122cf0e843",
      text=self.ai_output,
      voice="Rachel",
      model="eleven_multilingual_v2"
      )
      elevenlabs.play(audio)

  # Tasks Functions:

  def StartVýpočetVýživného(self):
    výpočet_výživného.gather_data()


# CLASS VÝPOČET VÝŽIVNÉHO ---------------------------------------------
class VýpočetVýživného():

  def __init__(self,
               výživné=0,
               čistý_příjem=0,
               počet_dětí=0,
               věk_dítěte=0,
               předškolní_věk=False,
               první_stupeň=False,
               druhý_stupeň=False,
               SŠ_VŠ=False):

    self.výživné = int(výživné)
    self.čistý_příjem = int(čistý_příjem)
    self.počet_dětí = int(počet_dětí)
    self.věk_dítěte = int(věk_dítěte)
    self.předškolní_věk = předškolní_věk
    self.první_stupeň = první_stupeň
    self.druhý_stupeň = druhý_stupeň
    self.SŠ_VŠ = SŠ_VŠ

  def gather_data(self):
    neplatí_výživné = False
    chatbot.ai_output = "Kolik je vašemu dítěti?"
    chatbot.GenerateAudio()
    věk_dítěte_first = input(' \nKolik je vašemu dítěti? ')
    self.věk_dítěte = int(věk_dítěte_first)
    if self.věk_dítěte <= 5 and self.věk_dítěte >= 0:
      print(' \nVaše dítě je předškolák')
      chatbot.ai_output = "Vaše dítě je předškolák"
      chatbot.GenerateAudio()
      self.předškolní_věk = True
    elif self.věk_dítěte > 5 and self.věk_dítěte <= 9:
      chatbot.ai_output = "Vaše dítě je na prvním stupni"
      chatbot.GenerateAudio()
      print(" \nVaše dítě je na prvním stupni")
      self.první_stupeň = True
    elif self.věk_dítěte >= 10 and self.věk_dítěte <= 14:
      chatbot.ai_output = "Vaše dítě je na druhém stupni"
      chatbot.GenerateAudio()
      print(" \nVaše dítě je na druhém stupni")
      self.druhý_stupeň = True
    elif self.věk_dítěte >= 15 and self.věk_dítěte <= 28:
      chatbot.ai_output = "Střední škola nebo vyšší vzdělávání"
      chatbot.GenerateAudio()
      print(" \nStřední škola nebo vyšší vzdělávání")
      self.SŠ_VŠ = True
    elif self.věk_dítěte > 28:
      chatbot.ai_output = "Vaše dítě už má pravděpodobně vystudované studium tudíž neplatíte výživné"
      chatbot.GenerateAudio()
      print(
          " \nVaše dítě už má pravděpodobně vystudované studium tudíž neplatíte výživné"
      )
      neplatí_výživné = True
    else:
      print("Neodpovídá, zkuste znovu")
      chatbot.ai_output = "Neodpovídá, zkuste znovu"
      chatbot.GenerateAudio()
    if not neplatí_výživné:
      self.calculate()
    else:
      chatbot.GeneralInput()

  def calculate(self):
    chatbot.ai_output = "Kolik je váš čistý příjem?"
    chatbot.GenerateAudio()
    čistý_příjem_first = input(' \nKolik je váš čistý příjem? ')
    self.čistý_příjem = int(čistý_příjem_first)
    if self.předškolní_věk:
      self.výživné = float(self.čistý_příjem) / 7.142857142857143

    elif self.první_stupeň is True:
      self.výživné = self.čistý_příjem / 6.25

    elif self.druhý_stupeň is True:
      self.výživné = self.čistý_příjem / 5.555555555555556

    elif self.SŠ_VŠ is True:
      self.výživné = self.čistý_příjem / 5

    self.výživné = int(self.výživné)
    výživné2 = str(self.výživné)
    chatbot.ai_output = (výživné2)
    chatbot.GenerateAudio()
    print(self.výživné)
    chatbot.GeneralInput()

výpočet_výživného = VýpočetVýživného()

# Výpočet věku -----------------------------------------------
def calculate_age(day, month, year):
  today = date.today()
  birthdate = date(year, month, day)
  age = today.year - birthdate.year - ((today.month, today.day) <
                                       (birthdate.month, birthdate.day))
  return age

def VýpočetVěku():
  try:
    day = input('Napiš den: ')
    month = input('Napiš měsíc: ')
    year = input('Napiš rok: ')
    age_result = calculate_age(int(day), int(month), int(year))
    print(f'Osoba je {age_result} let stará.')
  except:
    print('Nepovedlo se mi vypočítat věk, zkuste znova.')
  chatbot.GeneralInput()


chatbot = Chatbot()
chatbot.Start()
