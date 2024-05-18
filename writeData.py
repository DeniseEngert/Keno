import csv

header = ["roud", "duration"]


def writeData(data) -> None:
    with open('Rounds.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        #data.sort(key=lambda x: x[1])
        #writer.writerow(header)
        writer.writerows(data)
