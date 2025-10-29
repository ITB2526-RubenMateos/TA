import datetime

#Modificació: Demanar la data de naixement
dataActual = datetime.date.today()
anyActual = dataActual.year
mesActual = dataActual.month
print(dataActual)
print(anyActual)

anyNaixement = int(input("Any naixement"))
mesNaixement = int(input("Mes naixement"))

if (anyActual - anyNaixement) >= 10:
    if mesNaixement <= mesActual:
        print("Ets major d'edat")
else:
    print("Ets menor d'edat")
print("Programa Finalitzat")