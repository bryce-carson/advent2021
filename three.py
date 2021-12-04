with open("input3.txt") as d:
    data = d.readlines()

dataLength = len(data)
lineLength = len(data[0])
column = []
columnSum = []

for j in range(lineLength):
    columnData = []
    for i in range(dataLength):
        if not 48 <= ord(data[i][j]) <= 57:
            continue
        columnData.append(int(data[i][j]))
    column.append(columnData)
    if columnData != []:
        columnSum.append(sum(column[j]))

gammaRate = []
epsilonRate = []
for i in columnSum:
    if i/1000 > 0.5:
        gammaRate.append(1)
        epsilonRate.append(0)
    else:
        gammaRate.append(0)
        epsilonRate.append(1)

def binaryToDecimal(binaryNumber):
    length = len(binaryNumber)
    result = []
    for i in range(0,length):
        result.append(binaryNumber[-(i + 1)] * 2 ** i)
    return sum(result)

print(binaryToDecimal(gammaRate) * binaryToDecimal(epsilonRate))
