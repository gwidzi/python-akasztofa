import random
import math
import time
from os import system, name

def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

def action(valasztott, lehetosegek, ismert_string, szamok_db):
    kezdes = time.time()
    tippelt_betuk = []
    print(ismert_string)
    while lehetosegek > 0:
        tipp = input("Tipp: ").lower()
        if len(tipp) != 1 or not tipp.isalpha():
            print("Valami nem stimmel, egy betű kellene!\n")
            continue
        clear()
        
        tippelt_betuk.append(tipp)
        if tipp in valasztott:
            print(f"Eltaláltál {szamok_db[valasztott.count(tipp)-1]}!\n")
        else:
            print(f"{tipp.upper()} sajnos nincs benne!\n\n")
            lehetosegek -= 1
            
        a = 1
        print("[", end="")
        for l in tippelt_betuk:
            if a == len(tippelt_betuk):
                print(l, end="")
            else:
                print(f"{l}, ", end="")
            a += 1
        print("]")
        
        ismert_string = ""
        for betuk in valasztott:
            if betuk in tippelt_betuk:
                ismert_string += betuk + " "
            else:
                ismert_string += "_ "
        
        print(ismert_string)
        print("Fennmaradó lehetőségek:", lehetosegek)
        ido_str = ""
        if all(betuk in tippelt_betuk for betuk in valasztott):
            vege = time.time()
            t = round(vege - kezdes)
            if (t / 86400) > 1:
                ido_str += f"{t/86400} nap "
                t -= 86400
                break
            if (t / 3600) > 1:
                ido_str += f"{t/3600} óra "
                t -= 3600
                break
            if (t / 60) > 1:
                ido_str += f"{t/3600} perc "
                t -= 3600
                break
            ido_str += f"{t} másodperc"
            print(f"\n\nEltelt idő: {ido_str}")
            print("Gratulálok, eltaláltad!")
            break
        
        if lehetosegek == 0:
            vege = time.time()
            t = round(vege - kezdes)
            if (t / 86400) > 1:
                ido_str += f"{t/86400} nap "
                t -= 86400
                break
            if (t / 3600) > 1:
                ido_str += f"{t/3600} óra "
                t -= 3600
                break
            if (t / 60) > 1:
                ido_str += f"{t/3600} perc "
                t -= 3600
                break
            ido_str += f"{t} másodperc"
            print(f"\n\nEltelt idő: {ido_str}")
            print(f"Elfogytak a lehetőségeid. A szó {valasztott} volt")
            break
        
def main():
    szamok_db = ["egyet", "kettőt", "hármat", "négyet", "ötöt", "hatot", "hetet", "nyolcat", "kilencet"]
    with open("szavak.txt", "r") as fajl:
        szavak_db = fajl.read().splitlines()
    valasztott = random.choice(szavak_db)
    szavak_db.clear()
    hossz = len(valasztott)
    i = 0
    ismert_string = ""
    while i < hossz:
        ismert_string += "- "
        i += 1
    lehetosegek = round(math.log(hossz + 1, 2)) + 5
    print(f"Összesen {lehetosegek} lehetőséged van.")
    print(f"A kitalálandó szó {len(valasztott)} betű hosszú.")
    action(valasztott, lehetosegek, ismert_string, szamok_db)
main()