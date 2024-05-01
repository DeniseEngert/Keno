import json

with open("kenoData.json") as data:
    DATA = json.load(data)

TIP = DATA["Tips"]

def getEntriesPerYear(year):
    sumTips = 0
    sumKosten = 0
    sumTreffer = 0
    sumGewinne = 0

    for x in TIP:
        if x["Jahr"] == year:
            sumTips = sumTips + 1
            sumKosten = sumKosten + float(x["Kosten"])
            sumTreffer = sumTreffer + x["Treffer"]
            sumGewinne = sumGewinne + float(x["Gewinne"])

    print(f"Jahr: {year}\n Anzahl Tips: {sumTips},\n Anzahl Gewinne: {sumTreffer},\n Kosten: {sumKosten},\n Gewinne: {sumGewinne},\n GuV: {sumGewinne - sumKosten}")

def getLength():
    return len(TIP)


def getValues(key):
    summe = 0
    for x in TIP:
        i = float(x[key])
        summe += i
    return round(summe, 2)


def gewinneVerluste():
    guv = getValues("Gewinne") - getValues("Kosten")
    return guv

print("##### GESAMT #####")
print(f"Anzahl Tips:           {getLength()}")
print(f'Einsatz:               {getValues("Kosten")}')
print(f'Anzahl Gewinne:        {getValues("Treffer")}')
print(f'Gewinne:               {getValues("Gewinne")}')
print("-----------------------------")
print(f'GuV:                  {gewinneVerluste()}')
print("-----------------------------")
print()
print("##### PRO JAHR #####")
getEntriesPerYear(2024)



