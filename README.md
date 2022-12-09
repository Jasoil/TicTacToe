# OHPE_harkka

# Työn dokumentointi

1.  Työn aihe ja kuvaus

Työssä toteutettiin yksin tietokonetta vastaan pelattava ristinolla.
Pelissä ei ole graafista ulkoliittymää, vaan sitä pelataan terminaalissa (esim. vscode).
Pelissä voitetut pelit (erät) tallennetaan ja lopettaessa ilmoitetaan pelaajalle lopputulos.

2. Työn ratkaisuperiaate

Työ toteutettiin vscodessa.

3.  Työn rakenne

Työssä on main metodi, sekä tiedosto, joka sisältää käytetyt funktiot.
Peli toteutetaan main metodissa olevassa while loopissa, jossa kutsutaan funktioita.
Päyttäjän halutessa aloittaa uusi peli pelilauta, sekä mahdollisten numeroiden lista alustetaan alkuperäisen muotoiseksi.


4. Funktiot ja niiden suhteet

Fuktiot:
printlauta(), joka tulostaa kaksiuloitteisen arraylistan numeroita pelilaudan muotoon.
muutalauta(), joka sijoittaa laudalle numeron paikalle käyttäjän valitseman merkin, sekä tietokoneen vuorolla tietokoneen pelimerkin.
tarkastavoitto(), joka tarkastaa onko voron loputtua oikea voittorivi saavutettu (vaaka, pysty tai ristikkäin).
lopeta(), joka tulostaa tekstin käyttäjälle.

5. Kirjastojen käyttö

import random
import time

Työssä käytetään random kirjastoa, kun arvotaan tietokoneen valinta.
Työssä käytetään time kirjastoa tilanteissa, jossa koodi "nukkuu" toimintojen välissä

