import json

# winnersArray = []

with open("kenoData.json") as data:
    DATA = json.load(data)

TIPS = DATA["Tips"]


def getArrays() -> []:
    winnerWeeks = [x for x in TIPS if x["Treffer"] > 0]
    winnerTips = [x["Gewinner"] for x in winnerWeeks]
    winnerNumbers = []
    for x in winnerTips:
        for y in x:
            winnerNumbers.append(y)

    return winnerNumbers


def createDict(list) -> {}:
    countNumbers = {}
    for x in list:
        if str(x) in countNumbers:
            countNumbers[str(x)] += 1
        else:
            aux = {str(x): 1}
            countNumbers.update(aux)
    return countNumbers


list = sorted(getArrays())
cdict = createDict(list)

for key, value in cdict.items():
    print(f"Number: {key} - {value}")
