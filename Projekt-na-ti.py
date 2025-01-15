#import
import random #w celu wprowadzenia elementow losowosci
import sys #w celu wylaczania okna gry
import time #mozliwosc opoznienia programu
import os #w celu czyszczenia okna konsoli
#wartosci zmiennych
staty = 0
kasa = 50
kule = 50
harpun = 0
#kolory
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
# ascii pirackiego statku
pirate_ship = """
               |    |    |               
             (_(  (_(  (_(              
          /(___((___((___(             
         //(___((___((___((            
    __/\\\\\\____|____|____|_____        
--------\\                   /---------
   ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
     ^^^^      ^^^^     ^^^    ^^
          ^^^^      ^^^
"""
#przeciwnicy
przeciwnik = [
    {"nazwa": "rekin!", "zdrowie": 20},
    {"nazwa": "statek innych piratow!", "zdrowie": 15},
    {"nazwa": "statek floty krolewskiej!", "zdrowie": 25}
]
#def czyszczenia konsoli
def wyczysc():
    os.system('cls' if os.name == 'nt' else 'clear')
#def wydarzen
#funkcja animacji
def animacja():
    console_width = 80
    ship_width = len(pirate_ship.splitlines()[-1])


    for position in range(console_width + ship_width):
        wyczysc()
        padding = " " * (console_width - position if position < console_width else 0)
        for line in pirate_ship.splitlines():
            print(padding + line)
        time.sleep(0.01)
#walka
def losp():
    walkunia= random.choice(przeciwnik)
    return walkunia
def walka():
    global kule
    global harpun
    global kasa
    global staty
    while True:
        enemy = losp()
        print(f"Atakuje was przeciwnik: {enemy['nazwa']}")
        time.sleep(1)
        print(f"Aby pokonac tego przeciwnika potrzebujesz {enemy['zdrowie']} kul")
        time.sleep(1)
        if enemy["nazwa"] == "rekin!":
            if harpun >= 1:
                print("Posiadasz harpun dzieki ktoremu twoja zaloga moze poradzic sobie z rekinem bez uzycia kul!\n")
                time.sleep(2)
                plusik = random.randint(10,20)
                kasa = kasa + plusik
                print("Udaje wam sie pokonac rekina a za sprzedanie jego miesa otrzymujecie",plusik,"monet, lacznie posiadasz teraz",kasa,"monet")
                time.sleep(3)
                staty = staty + 1
                wybor0()
                break
            else:
                if kule >= enemy["zdrowie"]:
                    kule = kule - enemy["zdrowie"]
                    time.sleep(2)
                    print("Pokonujesz rekina! Pozostało Ci",kule,"kul")
                    time.sleep(3)
                    plusik = random.randint(10, 20)
                    kasa = kasa + plusik
                    print("Za sprzedanie jego miesa otrzymujecie", plusik,"monet, lacznie posiadasz teraz", kasa, "monet")
                    staty = staty + 1
                    time.sleep(2)
                    wybor0()
                    break
                else:
                    time.sleep(1)
                    print("Przegrywasz te walke, Twoj statek zatonal a Ty wraz z nim!")
                    time.sleep(1)
                    gameover()
                    break
        else:
            if kule >= enemy["zdrowie"]:
                kule = kule - enemy["zdrowie"]
                time.sleep(2)
                print("Pokonujesz wrogi statek! Pozostało Ci", kule, "kul")
                time.sleep(3)
                plusik = random.randint(10, 20)
                kasa = kasa + plusik
                print("Ze krzyni ktora zostala po zatopionym pokladzie udaje ci sie wydobyc",plusik,"monet\n teraz posiadasz ich:",kasa)
                staty = staty + 1
                time.sleep(2)
                wybor0()
                break
            else:
                time.sleep(1)
                print("Przegrywasz te walke, Twoj statek zatonal a Ty wraz z nim!")
                time.sleep(1)
                gameover()
                break
#pierwszy wybor po tutorialu
def wybor0():
    global kasa
    global harpun
    global kule
    while True:
        wyczysc()
        if staty <= 4:
            print("Co chcesz teraz zrobic?")
            print("PLYN dalej")
            print("SZUKAJ miejsca w ktorym zrobisz zakupy")
            choic = input("> ").strip().lower()
            if choic == "plyn":
                print("Decydujesz sie plynac dalej!")
                time.sleep(2)
                plyniesz()
                break
            elif choic == "szukaj":
                print("Zlecasz swojej zalodze wypatrywac miejsca w ktorym zrobicie zakupy")
                time.sleep(1)
                print("Napotykacie statek zaprzyjaznionych kupcow!")
                while True:
                    print("Co chcialbys kupic?")
                    print("Ilosc Twoich monet:", kasa)
                    print("KULE (koszt:25)")
                    print("HARPUN (koszt:50)")
                    print("NIC")
                    kupki = input("> ").strip().lower()
                    if kupki == "kule":
                        if kasa >= 25:
                            print("Kupiles 50 kul za 25 monet")
                            kule = kule + 50
                            kasa = kasa - 25
                            print("Teraz posiadasz", kasa, "monet, oraz", kule, "kul")
                            time.sleep(1)
                            wyczysc()
                            wybor0()
                        else:
                            wyczysc()
                            print("Masz za malo pieniedzy!")
                    elif kupki == "harpun":
                        if kasa >= 50:
                            print("Kupiles harpun za 50 monet")
                            kasa = kasa - 50
                            harpun = 1
                            print("Teraz posiadasz", kasa, "monet, oraz harpun")
                        else:
                            wyczysc()
                            print("Masz za malo pieniedzy!")
                    elif kupki == "nic":
                        print("Opuszczasz to miejsce")
                        time.sleep(2)
                        plyniesz()
                        break
                    else:
                        wyczysc()
                        print("Niepoprawny wybor!")

                break
            else:
                print("Niepoprawny wybor")
        else:
            wybor1()
    return
#etapy gry
def tutorial():
    print("Witaj!")

    print("W tej grze wcielisz sie w pirackiego kapitana statku poszukujacego zaginionego, pradawnego skarbu.")

    imie = input("Podaj swoje pirackie imie: ")

    print("Twoje imie to od teraz:", imie)

    statek = input("Podaj nazwe swojego pirackiego statku:")

    print("Twoj statek od teraz znany bedzie jako:", statek)

    print("Znany jako postrach siedmiu morz", imie, "wypywa wraz ze swoja zaloga na pokladzie", statek,
          "w celu odnalezienia \nzaginionego przed wiekami skarbu Czarnobrodego.")
    time.sleep(1)
    print("Podczas swoich poprzednich rejsow, zaloga statku", statek, "otrzymala polowe starozytnej mapy.")
    time.sleep(1)
    print("Chodza sluchy, ze druga czesc mapy posiada zaloga statku Maria.")
    time.sleep(1)
    print("Twoja zaloga wyposazona jest w", kule, "kul armatnich")
    time.sleep(1)
    print("Kule beda potrzebne Twojej zalodze do pokonywania przeciwnikow ktorych napotkasz na drodze")
    time.sleep(1)
    print("Pamietaj aby odpowiednio gospodarowac swoimi zasobami aby nie skonczyc na dnie morza!")
    time.sleep(1)
    print("Kazda walka lub interakcja przedstawi Ci Twoje opcje (na przyklad TAK lub NIE)")
    time.sleep(1)
    print(
        "Aby dokonać swojego wyboru wpisz słowo odpowiadające Twojej decyzji \n(bedzie ono zawsze napisane z duzych liter abys mial pewnosc o ktore slowo chodzi jednak nie jest wymagane abys Ty uzywal duzych liter)")
    time.sleep(1)

    print("(Aby dokonac wyboru wpisz TAK lub NIE)")

    while True:
        odpowiedz = input("Czy chcesz kontynuować? (tak/nie): ").strip().lower()

        if odpowiedz == "tak":
            print("Kontynuujesz gre!")
            time.sleep(2)
            wyczysc()
            start_gry()
            break
        elif odpowiedz == "nie":
            print("Zakanczasz gre")
            sys.exit()
        else:
            wyczysc()
            print("Nie rozumiem tej odpowiedzi. Proszę podaj 'tak' lub 'nie'.")

def start_gry():
    wybor0()

def plyniesz():
    animacja()
    wyczysc()
    print("Podczas wyprawy nagle wydarza sie cos niespodziewanego!")
    walka()

def wybor1():
    global staty
    while True:
        print(RED + "Na horyzoncie Twoja zaloga dostrzega statek Maria" + RESET)
        time.sleep(1)
        choic = input(
            "Czy chcesz teraz z nim walczyc w celu zdobycia pelnej mapy prowadzacej do skarbu (TAK lub NIE)?\n> ").strip().lower()
        if choic == "tak":
            boss()
            time.sleep(4)
            break
        elif choic == "nie":
            staty = 4
            wybor0()
        else:
            wyczysc()
            print("Niepoprawna odpowiedz!")

def boss():
    global kule
    global RED
    global GREEN
    global RESET
    while True:
        print("Rozpoczynasz walke z ostatnim przeciwnikiem!")
        time.sleep(0.5)
        print("Statek Maria jest bardzo silnym przeciwnikiem wiec do jego pokonania potrzebujesz az 100 kul")
        time.sleep(0.5)
        print("Nastepuje wymiana ognia!")
        time.sleep(0.5)
        print("Statek Maria nieustannie ostrzeliwuje Twoj statek lecz Ty i Twoja zaloga nie dajecie za wygrana!")
        if kule <= 100:
            print(RED + "Statek Maria zwyciezyl, Twoj statek zatonal, a statek Maria zdobywa pelna mape skarbow" + RESET)
            time.sleep(3)
            gameover()
        else:
            print(GREEN + "Zwycierzyles! Statek Maria tonie!" + RESET)
            time.sleep(1)
            print("Twoja zaloga wylawia dla Ciebie druga czesc mapy ktora byla w posiadaniu przeciwnika!")
            time.sleep(1)
            print("Zaloga Twojego statku teraz wyplywa w poszukiwaniu zaginionego skarbu!")
            time.sleep(1)
            print("To be continued...")
            time.sleep(5)
            sys.exit()

def gameover():
    wyczysc()
    print("Twoj statek zatonal, koniec gry!")
    time.sleep(2)
    sys.exit()

tutorial()