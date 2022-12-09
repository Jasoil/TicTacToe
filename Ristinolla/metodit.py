
#laudan attribuutit
lauta = [[1,2,3], [4,5,6], [7,8,9]]
numerot = [1,2,3,4,5,6,7,8,9]
rivit = 3
sarakkeet = 3

def printlauta():
    for i in range(rivit):
        print("\n-------------")
        print("|", end="")
        for j in range(sarakkeet):
            print("", lauta[i][j], end=" |")
    print("\n-------------")

def muutalauta(valinta, symboli):
    #rivi 1
    if(valinta == 1):
        lauta[0][0] = symboli
    elif(valinta == 2):
        lauta[0][1] = symboli
    elif(valinta == 3):
        lauta[0][2] = symboli
    #rivi 2
    elif(valinta == 4):
        lauta[1][0] = symboli
    elif(valinta == 5):
        lauta[1][1] = symboli
    elif(valinta == 6):
        lauta[1][2] = symboli
    #rivi3
    elif(valinta == 7):
        lauta[2][0] = symboli
    elif(valinta == 8):
        lauta[2][1] = symboli
    elif(valinta == 9):
        lauta[2][2] = symboli



def tarkistavoitto():
    #vaaka
    if(lauta[0][0] == "x" and lauta[0][1] == "x" and lauta[0][2] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[0][0] == "0" and lauta[0][1] == "0" and lauta[0][2] == "0"):
        print("0 voitti pelin!")
        return True
    elif(lauta[1][0] == "x" and lauta[1][1] == "x" and lauta[1][2] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[1][0] == "0" and lauta[1][1] == "0" and lauta[1][2] == "0"):
        print("0 voitti pelin!")
        return True
    elif(lauta[2][0] == "x" and lauta[2][1] == "x" and lauta[2][2] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[2][0] == "0" and lauta[2][1] == "0" and lauta[2][2] == "0"):
        print("0 voitti pelin!")
        return True

    #pysty
    elif(lauta[0][0] == "x" and lauta[1][0] == "x" and lauta[2][0] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[0][0] == "0" and lauta[1][0] == "0" and lauta[2][0] == "0"):
        print("0 voitti pelin!")
        return True
    elif(lauta[0][1] == "x" and lauta[1][1] == "x" and lauta[2][1] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[0][1] == "0" and lauta[1][1] == "0" and lauta[2][1] == "0"):
        print("0 voitti pelin!")
        return True
    elif(lauta[0][2] == "x" and lauta[1][2] == "x" and lauta[2][2] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[0][2] == "0" and lauta[1][2] == "0" and lauta[2][2] == "0"):
        print("0 voitti pelin!")
        return True
    #ristikkäin
    elif(lauta[0][0] == "x" and lauta[1][1] == "x" and lauta[2][2] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[0][0] == "0" and lauta[1][1] == "0" and lauta[2][2] == "0"):
        print("0 voitti pelin!")
        return True
    elif(lauta[2][0] == "x" and lauta[1][1] == "x" and lauta[0][2] == "x"):
        print("x voitti pelin!")
        return True
    elif(lauta[2][0] == "0" and lauta[1][1] == "0" and lauta[0][2] == "0"):
        print("0 voitti pelin!")
        return True
    else:
        return False

    
def lopeta():
      print("\n***Peli päättyi***\n")