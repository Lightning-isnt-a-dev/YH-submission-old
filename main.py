from classes import *
from os import system, path
from os import name as osname
from art import text2art
from random import shuffle
import pickle


#Functions
def wait():
  input("Paina enter jatkaaksesi.")
  clearScreen()
  return


def GetPlayerInfo(SaveDict):
  omaisuus = 15000000000
  mult = 1.0

  nimi = str(input("Mikä on sinun nimesi? \n"))
  
  if nimi in SaveDict.keys():
    clearScreen()
    print(f"\nMoi {nimi}! Sinulla on {SaveDict[nimi][0]}€ ja sinun raha kerroin on {SaveDict[nimi][1]}.")
    print("Yritysidea vaihtoehdot ovat:\n")
    omaisuus, mult = SaveDict[nimi]
    wait()
    

  else:
    print(f"\nTervetuloa {nimi}! Yritysidea vaihtoehdot ovat:\n")

  työ = NewJob()

  return nimi, työ, omaisuus, mult

#valitse uus työ
def NewJob():
  TYÖT = {
    "Helppo" : ["kahvila"],
    "Vaikea" : ["hesburger"]
  }
  VALIKOIMAT = ["kahvila", "hesburger"]
  työ = ""
  
  for taso, työt in TYÖT.items():
    print(f"{text2art(f'---{taso}---')}")
    for työ in työt:
      print("•",työ)
    print("\n\n\n\n\n")

  print("\nValitse työsi.")
  while True:
    työ = str(input(""))

    if työ.lower() not in VALIKOIMAT:
      print("\nYritysidea ei ole listassa. Valitse työsi uudelleen.")
      continue

    break

  return työ


#kysyminen
def kysy(kysymykset, Player):
  print(text2art(Player.GetJob()))
  omaisuus = Player.GetMoney()
  kysymyksetOmaisuus = 0

  TierOptionsDict = {}

  kysymyksetKeys = list(kysymykset.keys())

  shuffle(kysymyksetKeys)
  
  for index in kysymyksetKeys:
    kysymys = index
    vastausLista = kysymykset[index]
    
    print(kysymys + "\n")

    for value in vastausLista:
      print(value[0])

    while True:
      try:
        vastaus = int(input("\nnumero: \n"))

      except ValueError:
        print("Vastaus ei ollut numero.")
        continue

      if vastaus not in range(0, len(vastausLista)):
        print("Vastaus ei ole listassa.")
        continue

      raha = vastausLista[vastaus][2]*Player.GetMultiplier()
      
      if raha < 0:
        kysymyksetOmaisuus -= -raha
      else:
        kysymyksetOmaisuus += raha
        
      
      print(f"\n{vastausLista[vastaus][1]} vastaus. Saat {raha}€. Sinulla on nyt {omaisuus+kysymyksetOmaisuus}€.")

      
      try:
        TierOptionsDict[vastausLista[vastaus][1]]
        
      except KeyError:
        TierOptionsDict[vastausLista[vastaus][1]] = 1

      
      TierOptionsDict[vastausLista[vastaus][1]] += 1

      
      if omaisuus+kysymyksetOmaisuus < 0:
        exit(f"\n\nSinulla ei ole enää raha, Hävisit pelin. Onnea seuraavalla keralla {Player.GetName()}!")

      wait()
      
      print(text2art(Player.GetJob()))
      break

  
  print(f'Hyvin tehty {Player.GetName()}. Sait {kysymyksetOmaisuus}€ tästä työstä, ja sinulla on nyt {omaisuus+kysymyksetOmaisuus}€.\n')
  
  print("Tässä on valitsemiesi hyvien ja huonojen vastausten määrä:")
  for tier, amount in TierOptionsDict.items():
    print(f"{tier}: {amount}")

  input("\nPaina enter jatkaaksesi.")
  return omaisuus+kysymyksetOmaisuus


def kahvila(Player):
  kahvilaKysym = {
    
      "Miksi perustitte tämän kahvilan?": [
       ("'0' - Koska haluan ansaita lisää rahaa", "hyvä", 100),
       ("'1' - Tuli vain mieleen eräänä päivänä", "hyväksyttävä", 50),
       ("'2' - Koska miksi ei", "huono", -60)],
    
      "Miksi kahvilaanne kannattaisi sijoittaa?": [
       ("'0' - Täällä on kivaa väkeä", "hyväksyttävä", 50),
       ("'1' - Koska tämä on paras paikka", "huono", -30),
       ("'2' - Tämä kahvila tuottaa paljon", "hyvä", 100)],
    
      "Mikä tekee teidän kahvilastanne erityisen?": [
       ("'0' - Tämä kahvila ei maksa veroja", "hirveä", -70),
       ("'1' - Kahvilan sijainti", "hyväksyttävä", 50),
       ("'2' - Kahvilan hyvä yhteisöllisyys ja tuotteiden tuoreus ", "hyvä", 100)],
    
      "Miten paljon rahaa kahvilanne tuottaa vuodessa?": [
       ("'0' - 100 000€", "hyväksyttävä", 50),
       ("'1' - Kohtuullisesti, mutta yritämme parantaa tuotantoa jatkuvasti", "hyvä", 100),
       ("'2' - Enemmän kuin sinun isäsi", "kauhea", -100)],

      "Miten hyvin hoidatte tätä paikkaa?": [
       ("'0' - Täällä siivotaan joka päivä ", "hyvä", 100),
       ("'1' - Puhtaudesta huolehditaan rahojen jälkeen", "hirveä", -75),
       ("'2' - Melko usein", "hyväksyttävä", 50)],
  }

  print("Tässä pelitilassa olet kahvilan omistaja.")
  print("Kirjoita numero 0, 1 tai 2 vastataksesi kysymyksiin.\n")

  wait()
  
  return kysy(kahvilaKysym, Player)


def hesburger(Player):
  heseKysym = {
    
       "Mitä varten avasitte tämän Hesburgerin?": [
       ("'0' - Olen miettinyt hesburgerin avaamista jo kauan ja päätin lopulta tehdä juuri niin. Isoin syyni tekemääni päätökseen oli raha, sillä olin työtön ja en löytänyt montaa eri vaihtoehtoa.", "hyvä", 50),
       ("'1' - Avasin sen jotta voisin saada itselleni hieman tuloja, sillä olin työtön melko kauan", "hyväksyttävä", 25),
       ("'2' - Hesburgerin perustaminen tuli vain mieleeni eräänä päivänä", "huono", -100)],

      "Miksi Hesburgerinne olisi hyvä sijoituskohde?": [
       ("'0' - Kaikki rakastavat roskaruokaa, joten investoiminen hesburgeriin ei olisi huono idea.", "hyväksyttävä", 10),
       ("'1' - Tyopaikan ilmapiiri on loistava ja rahaa tulee kassaan paljon.", "huono", -100),
       ("'2' - Paikkamme tuottaa paljon jo nyt, mutta jos saisimme rahoitusta voisimme tuottaa paljon enemmän.", "hyvä", 25)],

      "Mikä tekee teidän Hesburgeristanne erityisen?": [
       ("'0' - Hesburgerimme on oikeasti huumebisnes joka on peitetty näyttämään vain pikaruokaravintolalta.", "hirveä", -1000000),
       ("'1' - Tiimityömme on erinomaista ja valitsemme työntekijämme huolella.", "hyväksyttävä", 25),
       ("'2' - Sijaintimme on suositussa paikassa, jonka takia tuottomme on plussalla ja motivaatiomme korkeana.", "hyvä", 50)],

      "Miten paljon rahaa Hesburgerinne tuottaa vuodessa?": [
       ("'0' - 100 000€ kuukaudessa", "hyväksyttävä", 20),
       ("'1' - Enemmän kuin sinun isäsi", "kauhea", -150),
       ("'2' - Kohtuullisesti, mutta yritämme parantaa tuottoamme jatkuvasti", "hyvä", 50)],

      "Miten hyvin hoidatte tätä paikkaa?": [
       ("'0' - Täällä koko ravintola siivotaan joka päivä ", "hyvä", 25),
       ("'1' - Puhtaudesta huolehditaan rahojen jälkeen", "hirveä", -100),
       ("'2' - Melko hyvin keittiö siivotaan viikottain ja muu ravintola päivittäin", "hyväksyttävä", 15)],
  }

  print("Tässä pelitilassa olet Hesburgerin omistaja.")
  print("Kirjoita numero 0, 1 tai 2 vastataksesi kysymyksiin.\n")

  wait()

  return kysy(heseKysym, Player)


def clearScreen():
  system('cls' if osname == 'nt' else 'clear')

def SaveGame(Player):
  SaveDict = {}
  
  if path.exists("SaveFile"):
    with open("SaveFile", "rb") as savefile:
      SaveDict = pickle.load(savefile)

  with open("SaveFile", "wb") as savefilewrite:
    name, bal, mult = Player.SavePlayer()
    SaveDict[name] = (bal, mult)
    pickle.dump(SaveDict, savefilewrite)


def lidl(Player):
  clearScreen()
  
  Kaupassa = {
    "1" : ("Rahan Kerroin - Nostaa rahakerrointa 0,2:lla jokaisesta ostoksesta.", 1000, Player.IncreaseMultiplier),

    "2" : ("Osta Maa - Voitat pelin (aloitat pelin alusta, rahat ja rahan kerroin nollataan)", 100000, Player.ClearSave)
  }
  
  while True:
    print(text2art("Lidl"))
    for listing, ItemTuple in Kaupassa.items():
      desc, cost, _ = ItemTuple
      print(f"'{listing}' = {desc} Se maksaa {cost}€\n")
    
    ans = input("Mitä haluat ostaa? (E jos haluat poistua)\n")

    if ans.lower() == "e":
      clearScreen()
      return

    elif ans in Kaupassa.keys():
      desc, cost, action = Kaupassa[ans]
      BankSay, HasMoney = Player.Withdraw(cost)
      
      if HasMoney:
        action()

        if ans == "1":
          print("Lisäsit rahakerroin 0,2:lla. Sinun rahakerroin on nyt ", Player.GetMultiplier())
        
        elif ans == "2":
          SaveGame(Player)
          clearScreen()
          exit("\nVoitit pelin! Heippa! :)")
          
        print(BankSay)
      else:
        print(BankSay)
          
    else:
      print("\nValikoima ei ole kaupassa.\n")
      
    input("\nPaina enter jatkaaksesi.")
    clearScreen()

#Main
if __name__ == "__main__":
  clearScreen()
  SaveDict = {}
  
  if path.exists("SaveFile"):
    with open("SaveFile", "rb") as save:
      SaveDict = pickle.loads(save.read())

  print(text2art("Yritys   Hyva"))
  
  Player = Person(*GetPlayerInfo(SaveDict))

  clearScreen()

  print(
      f"\nMoi {Player.GetName()}! Tervetuloa pelamaan haastattelupeliämme! "
      f"Valitsit yritysidean: {Player.GetJob()}.\n"

      "Tehtävänäsi on kerätä rahaa sijoittajilta vastaamalla heidän kysymyksiinsä oikein.\n\n"

      "Jos vastaat hyvin, saat rahaa.\nJos vastaat huonosti et saa rahaa."

      "\n\nJos häviät kaikki rahasi, peli päättyy, niin ole varovainen!\n"
      f"Sinulla on {Player.GetMoney()}€.\n\n "
  )

  wait()

  while True:
      clearScreen()
      print(text2art("Valikko"))

      if Player.GetMoney() >= 100000:
        print("\nVoit mennä lidliin ostamaan maata ja voittamaan pelin!\n")
    
      ans = input("\nHaluatko mennä kauppaan vai töihin, vai haluatko mennä valitsemaan uuden työn? (L/T/UT) \nJos haluat poistua, kirjoita 'E'\n")
    
      if ans.lower() == "l":
        lidl(Player)
        continue
        
      elif ans.lower() == "t":
        clearScreen()
        Player.Deposit(locals()[Player.GetJob()](Player))
        continue

      elif ans.lower() == "ut":
        clearScreen()
        Player.Job(NewJob())
        continue

      elif ans.lower() == "e":
        SaveGame(Player)
        exit(f"Hyvin tehty! Sinulla on nyt {Player.GetMoney()}€. Rahahasi on tallenettu nimellä {Player.GetName()}. Rahankertoimesi on {Player.GetMultiplier()}.")

      else:
        print("Vastaus ei ole valikoimassa.")
        wait()
      