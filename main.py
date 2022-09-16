import csv
import matplotlib.pyplot as plt
import pandas
import numpy as np

file = open('data.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
  rows.append (row)
print(rows)
file.close()

#clean the data
for i in range(len(rows[0])):
  rows[0][i] = int(rows[0][i])
print(rows)

plt.bar(header,rows[0])
plt.title('Covid Data')
plt.xlabel('Days')
plt.ylabel('Number of Cases')
plt.grid()
plt.show()