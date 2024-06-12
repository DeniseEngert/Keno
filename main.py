import random
import sys
import time
import writeData as wd

numbArray = []
numbTip = []
numbZiehung = []
treffer = 0
#versuche = 0
ziehungen = []
data = []

sort = False


def fillArray() -> None:  # fills numbArray
    global numbArray
    for x in range(1, 71):
        numbArray.append(x)


def ziehung() -> None:  # choses 20 random numbers from numbArray, saves them in numbZiehung
    global numbZiehung
    global numbArray

    fillArray()

    for x in range(0, 20):
        z = random.choice(numbArray)
        numbZiehung.append(z)
        numbArray.remove(z)

    numbArray = []


def tip(typ: int) -> None:  # choses x numbers from numbArray as the betting, saves them in numbTip
    global numbArray
    global numbTip
    global sort

    fillArray()

    for x in range(0, typ):
        sort = not sort
        z = random.choice(numbArray)
        numbTip.append(z)
        numbArray.remove(z)
        numbArray.sort(reverse=sort)


def auswertung() -> None:  # compares numbZiehung with numbTip
    global treffer

    for x in numbTip:
        for n in numbZiehung:
            if x == n:
                treffer += 1


def getNumbers(typ: int) -> None:  # starts rounds
    ziehung()
    tip(int(typ))
    auswertung()


def getWinner() -> []:  # identifies tip with fastest win
    winversuche = ziehungen[0]["versuche"]
    indx = 0

    for x in range(len(ziehungen)):
        if ziehungen[x]["versuche"] < winversuche:
            winversuche = ziehungen[x]["versuche"]
            indx = x

    return ziehungen[indx]


def runTilWin(typ: int) -> None:
    #global versuche
    global treffer
    global numbArray
    global numbZiehung
    global numbTip

    for x in range(0, 10):
        aux = {}
        versuche = 0
        numbArray = []
        numbZiehung = []
        numbTip = []
        treffer = 0

        start = time.time()
        while treffer <= (typ - 1):
            aux = {}
            treffer = 0
            numbArray = []
            numbZiehung = []
            numbTip = []

            versuche += 1

            getNumbers(typ)
        end = time.time()
        data.append([x + 1, end - start])

        print("--------------------")
        print("Runde: ", x + 1)
        aux.update({"versuche": versuche, "zahlen": numbTip})
        ziehungen.append(aux)
        print("Anzahl Versuche: ", "{:,}".format(versuche))
        print("gezogene Zahlen: ", sorted(numbZiehung))
        print("getippte Zahlen: ", sorted(numbTip))

    winner = getWinner()
    print()
    print("===================")
    print("Winner:\n*** Versuche:", winner["versuche"], "\n*** Tip:", sorted(winner["zahlen"]))
    print("===================")
    wd.writeData(data)


if __name__ == '__main__':
    arg = sys.argv[1]
    runTilWin(int(arg))

# 9 Richige:
