import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Rounds.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

plt.plot(x, y)

# plt.bar(x, y, color='g', width=0.72, label="Duration")
# plt.xlabel('Round')
# plt.ylabel('Duration')
# plt.title('Duration of Rounds')
# plt.legend()
plt.show()
