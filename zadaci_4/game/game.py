import random
import json
import datetime

tajniBroj = random.randint(1, 30)
brojPokusaja = 0
netocniPokusaji = []

def mojaFunkcija(e):
    return e["broj pokusaja"]

with open("rangLista.txt", "r") as bodovnaLista:
    najRezultat = json.loads(bodovnaLista.read())
    najRezultat.sort(key= mojaFunkcija)

for rijecnikRezultata in najRezultat[:3]:
    print("Ime igrača: " + (rijecnikRezultata["ime igraca"]))
    print(str(rijecnikRezultata["broj pokusaja"]) + " pokušaja, datum i vrijeme igre: " + rijecnikRezultata.get("datum"))
    print("Traženi broj:",rijecnikRezultata["tajni broj"])
    print("Netočni pokušaji:",rijecnikRezultata["netocni pokusaji"])


imeIgraca = str(input("Molimo upišite vaše ime: "))
print("Dobro došli " + str(imeIgraca) + "!")

while True:
    pogodak = int(input("Pokušajte pogoditi tajni broj između 1 i 30: "))
    netocniPokusaji.append(pogodak)
    brojPokusaja += 1

    if pogodak == tajniBroj:
        netocniPokusaji = netocniPokusaji[:-1]
        najRezultat.append({"ime igraca": imeIgraca, "broj pokusaja": brojPokusaja, "datum": str(datetime.datetime.now()), "tajni broj": tajniBroj, "netocni pokusaji": netocniPokusaji})
        with open("rangLista.txt", "w") as bodovnaLista:
            bodovnaLista.write(json.dumps(najRezultat))

        print("Točno! Pogodio si tajni broj. Čestitam! Tajni broj je " + str(tajniBroj))
        print("Pogodio si iz " + str(brojPokusaja), "pokušaja.")
        break

    elif pogodak > tajniBroj:
        print("Broj " + str(pogodak), "je veći od traženog. Probaj s nekim manjim.")

    elif pogodak < tajniBroj:
        print("Broj " + str(pogodak), "je manji od traženog. Probaj s nekim većim.")
