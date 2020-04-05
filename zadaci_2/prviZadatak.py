
milja = 0.6214

print("Dobrodošli u program za preračunavanje udaljenosti.")
print("Ukoliko želite preračunati kilometre u milje, došli ste na pravo mjesto.")
print("Sve što trebate učiniti je unijeti udaljenost koju želite preračunati, izraženu cijelim brojem,")
print("a program će sam učiniti ostalo.")

while True:

    kilometri = int(input("Molimo unesite broj kilometara: "))

    print("Udaljenost od "+ str(kilometri), "kilometara iznosi " + str(kilometri * milja), "milja.")

    odgovor = input("Želite li preračunati još neku udaljenost (d/n) ? ")

    if  odgovor != "d":
        print("Hvala Vam na posjeti.")
        break



