while True:
    str_one = input("Molimo unesite tekst koji sadrži velika slova: ")
    print(str_one.lower())

    nastaviti = input("Nastaviti? (d/n) ")
    if nastaviti != "d":
       break