from metodit import *
import random
import time


print("\n***Tervetuloa***\n")
time.sleep(1)
while True:
        psymboli = input("Valitse pelimerkki syöttämällä x tai 0 (nolla): ")
        if (psymboli == "x") or (psymboli == "0"):
            time.sleep(0.5)
            print("\n***Lukitaan symboli: " + psymboli + "***")
            time.sleep(2)
            if psymboli == "x":
                  bsymboli = "0"
            elif psymboli == "0":
                  bsymboli = "x"
            break
        else:
            print("Syötteen on oltava x tai 0!")
            continue
      #botti
printlauta()

#pelaaja
vuoro = 0
while(vuoro != "null"):
      while(vuoro == 0):
            psiirto = input("\nSyötä numero, jonka paikalle haluat sijoittaa pelimerkin tai 'lopeta' lopettaaksesi: ")
            if psiirto == "lopeta":
                  vuoro = "null"
                  lopeta()
            elif int(psiirto) < 1 or int(psiirto) > 9:
                  print("Siirron tulee olla 0-9 väliltä!") 
                  break
            elif psiirto != "lopeta":
                  print("Valitaan ruutu " + psiirto)
                  time.sleep(1)
                  vuoro = 1
                  muutalauta(int(psiirto), psymboli)
                  printlauta()
                  time.sleep(2)
                  print("\n***Tietokoneen vuoro***")
                  time.sleep(1)
                  while(vuoro == 1):
                        print("Tietokone valitsee...")
                        time.sleep(2)
                        bsiirto = random.randint(1,9)
                        muutalauta(bsiirto, bsymboli)
                        printlauta()
                        vuoro = 0
                        print("\n***Pelaajan vuoro***")

