# izgled
kosa = {"crna": "CCAGCAATCGC", "smeđa": "GCCAGTGCCG", "plava": "TTAGCTATCGC"}
lice = {"oštro": "GCCACGG", "okruglo": "ACCACAA","ovalno": "AGGCCTCA", }
bojaOciju = {"plava": "TTGTGGTGGC", "zelena": "GGGAGGTGGC", "smeđa": "AAGTAGTGAC"}
spol = {"ženski": "TGAAGGACCTTC", "muški": "TGCAGGAACTTC"}
rasa = {"bijela": "AAAACCTCA", "crna": "CGACTACAG", "azijat": "CGCGGGCCG"}


# osumnjičeni
eva = {"spol": "ženski", "rasa": "bijela", "kosa": "plava", "oči": "plava", "lice": "ovalno"}
larisa = {"spol": "ženski", "rasa": "bijela", "kosa": "smeđa", "oči": "smeđa", "lice": "ovalno"}
matej = {"spol": "muški", "rasa": "bijela", "kosa": "crna", "oči": "plava", "lice": "ovalno"}
miha = {"spol": "muški", "rasa": "bijela", "kosa": "smeđa", "oči": "zelena", "lice": "oštro"}


with open("dna.txt", "r") as dnaKod:
    niz = dnaKod.read()


osumnjiceni = {}


for x in kosa:
    if kosa[x] in niz:
       osumnjiceni["kosa"] = x

for x in lice:
    if lice[x] in niz:
       osumnjiceni["lice"] = x

for x in bojaOciju:
    if bojaOciju[x] in niz:
       osumnjiceni["oči"] = x

for x in spol:
    if spol[x] in niz:
       osumnjiceni["spol"] = x

for x in rasa:
    if rasa[x] in niz:
       osumnjiceni["rasa"] = x


if osumnjiceni == eva:
    print("Eva je pojela sladoled!")
elif osumnjiceni == larisa:
    print("Larisa je pojela sladoled!")
elif osumnjiceni == miha:
    print("Miha je pojeo sladoled!")
elif osumnjiceni == matej:
    print("Matej je pojeo sladoled!")

