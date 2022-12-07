#laudan signatuuri
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
    if(valinta == 2):
        lauta[0][1] = symboli
    if(valinta == 3):
        lauta[0][2] = symboli
    #rivi 2
    if(valinta == 4):
        lauta[1][0] = symboli
    if(valinta == 5):
        lauta[1][1] = symboli
    if(valinta == 6):
        lauta[1][2] = symboli
    #rivi3
    if(valinta == 6):
        lauta[2][0] = symboli
    if(valinta == 7):
        lauta[2][1] = symboli
    if(valinta == 8):
        lauta[2][2] = symboli

