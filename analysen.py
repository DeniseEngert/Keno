import json

with open("kenoData.json") as data:
    DATA = json.load(data)

TIP = DATA["Tips"]


def getEntriesPerYear(year) -> None:
    # sums up values for different key in a certain year
    sumTips = 0
    sumKosten = 0
    sumTreffer = 0
    sumGewinne = 0

    for x in TIP:
        if x["Jahr"] == year:
            sumTips += 1
            sumKosten += float(x["Kosten"])
            sumTreffer += x["Treffer"]
            sumGewinne += float(x["Gewinne"])

    print(
        f"Jahr: {year}\n Anzahl Tips: {sumTips},\n Anzahl Gewinne: {sumTreffer},\n Kosten: {sumKosten},\n ∑ Gewinne in €: {sumGewinne},\n GuV: {sumGewinne - sumKosten}")


def getLength() -> int:
    return len(TIP)


def getValues(key) -> float:
    # sums up values for different keys
    summe = 0
    for x in TIP:
        i = float(x[key])
        summe += i
    return round(summe, 2)


def gewinneVerluste() -> float:
    guv = getValues("Gewinne") - getValues("Kosten")
    return guv


def trefferVSmisses() -> str:
    sum_treffer = 0
    sum_misses = 0

    for x in TIP:
        if x["Treffer"] > 0:
            sum_treffer += x["Treffer"]
        if x["MISS"] > 0:
            sum_misses += x["MISS"]

    return f"Treffer: {sum_treffer}, Misses: {sum_misses}"


print("##### GESAMT #####")
print(f"Anzahl Tips:           {getLength()}")
print(f'Einsatz:               {getValues("Kosten")}')
print(f'Anzahl Gewinne:        {getValues("Treffer")}')
print(f'∑ Gewinne     :        {getValues("Gewinne")} €')
print("-----------------------------")
print(f'GuV:                  {gewinneVerluste()}')
print("-----------------------------")
print(trefferVSmisses())
print()
print("##### PRO JAHR #####")
getEntriesPerYear(2024)
