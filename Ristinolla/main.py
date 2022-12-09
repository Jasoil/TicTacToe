from metodit import *
import random
import time
numerot = [1,2,3,4,5,6,7,8,9]

print("\n***Tervetuloa***\n")
time.sleep(1)
while True:
        psymboli = input("Valitse pelimerkki syöttämällä x tai 0 (nolla): ")
        if (psymboli == "x") or (psymboli == "0"):
            time.sleep(0.5)
            print("\n***Lukitaan symboli: " + psymboli + "***")
            time.sleep(1)
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
while(vuoro != "null"):
      while(vuoro == 0):
            psiirto = input("\nSyötä kokonaisluku, jonka paikalle haluat sijoittaa pelimerkin tai 'lopeta' lopettaaksesi: ")
            if psiirto == "lopeta":
                  vuoro = "null"
                  print("Kiitos pelistä!")
                  lopeta()
            elif int(psiirto) not in numerot:
                  print("\nSyöte ei ollut 1 ja 9 väliltä tai se oli jo valittu!")
                  break
            elif psiirto != "lopeta":
                  numerot.remove(int(psiirto))
                  print("Valitaan ruutu " + psiirto)
                  time.sleep(1)
                  vuoro = 1
                  muutalauta(int(psiirto), psymboli)
                  printlauta()
                  print("")
                  if tarkistavoitto() == True:
                        vuoro = "null"
                        lopeta()
                  time.sleep(1)
                  #botti
                  while(vuoro == 1):
                        print("\n***Tietokoneen vuoro***")
                        time.sleep(1)
                        print("Tietokone valitsee...")
                        time.sleep(1)
                        bsiirto = numerot.pop(random.randint(0,len(numerot)-1))
                        muutalauta(bsiirto, bsymboli)
                        printlauta()
                        tarkistavoitto()
                        vuoro = 0
                        print("\n***Pelaajan vuoro***")
