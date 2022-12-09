from funktiot import *
import random
import time


print("\n***Tervetuloa***\n")
time.sleep(0.5)
while True:
        psymboli = input("Valitse pelimerkki syöttämällä x tai 0 (nolla): ")
        if (psymboli == "x") or (psymboli == "0"):
            time.sleep(0.25)
            print("\n***Lukitaan symboli: " + psymboli + "***")
            time.sleep(0.75)
            if psymboli == "x":
                  bsymboli = "0"
            elif psymboli == "0":
                  bsymboli = "x"
            break
        else:
            print("Syötteen on oltava x tai 0!")
            continue
printlauta()

#pelaaja
vuoro = 0
ppisteet = 0
bpisteet = 0
while(vuoro != "null"):
      while(vuoro == 0):
            psiirto = input("\nSyötä kokonaisluku, jonka paikalle haluat sijoittaa pelimerkin tai 'lopeta' lopettaaksesi: ")
            if psiirto == "lopeta":
                  vuoro = "null"
                  print("Kiitos pelistä!")
                  break
            try:
                  if int(psiirto):
                        pass
            except:
                  print("Syöte ei ollut kokonaisluku tai 'lopeta'!")
                  break
            if int(psiirto) not in numerot:
                  print("Syöte ei ollut 1 ja 9 väliltä tai se oli jo valittu!")
                  break
            elif psiirto != "lopeta":
                  numerot.remove(int(psiirto))
                  print("Valitaan ruutu " + psiirto)
                  time.sleep(0.25)
                  vuoro = 1
                  muutalauta(int(psiirto), psymboli)
                  printlauta()
                  print("")
                  if tarkistavoitto() == True:
                        vuoro = "null"
                        ppisteet = ppisteet + 1
                        lopeta()
                  time.sleep(2)
                  #botti
                  while(vuoro == 1):
                        print("\n***Tietokoneen vuoro***")
                        time.sleep(0.25)
                        print("Tietokone valitsee...")
                        time.sleep(1)
                        bsiirto = numerot.pop(random.randint(0,len(numerot)-1))
                        print("Tietokone valitsi paikan: " + str(bsiirto))
                        time.sleep(0.5)
                        muutalauta(bsiirto, bsymboli)
                        printlauta()
                        print("")
                        vuoro = 0
                        if tarkistavoitto() == True:
                              vuoro = "null"
                              bpisteet = bpisteet + 1
                              lopeta()
                        print("\n***Pelaajan vuoro***")
      print("\nPelaajan pisteet: " + str(ppisteet))
      print("Tietokoneen pisteet: " + str(bpisteet))
      uusipeli = int(input("\nSyötä 1 pelataksesi uudestaan tai 2 lopettaaksesi: "))
      if uusipeli == 2:
            vuoro = "null"
            print("\n***Peli päättyi toivottavasti pidit peleistä!***\n")
            if (ppisteet > bpisteet):
                  print("Kokonaistulos: Pelaaja voitti pelin!")
            elif (ppisteet < bpisteet):
                  print("Kokonastulos: Tietokone voitti pelin!")  
            else:
                  print("Kokonaistulos: Tasapeli!")
      elif uusipeli == 1:
            vuoro = 0
            muutalauta(1,1)
            muutalauta(2,2)
            muutalauta(3,3)
            muutalauta(4,4)
            muutalauta(5,5)
            muutalauta(6,6)   
            muutalauta(7,7)
            muutalauta(8,8)
            muutalauta(9,9)       
            numerot = [1,2,3,4,5,6,7,8,9]
            printlauta()
