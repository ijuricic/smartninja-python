

unesenaVrijednost = int(input("Molimo unesite jedan broj od 1 do 100: "))

for i in range(unesenaVrijednost):

    if i % 5 == 0 and i % 3 == 0:
        i="fizz buzz"

    elif i % 3 == 0:
        i="fizz"

    elif i % 5 == 0:
        i="buzz"

    print (i)



