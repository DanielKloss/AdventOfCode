file = open("day1.txt", "r")

lines = file.readlines()

listOne = []
listTwo = []

for line in lines:
    splits = line.split("   ")
    listOne.append(int(splits[0]))
    listTwo.append(int(splits[1]))

#PART 1

listOne.sort()
listTwo.sort()

results = []

for counter in range(len(listOne)):
    result = abs(listOne[counter] - listTwo[counter])
    results.append(result)

total = 0

for result in results:
    total += result

print(total)

##PART 2

results = []
total = 0

for counter in range(len(listOne)):
    numberFound = 0
    for counter2 in range(len(listTwo)):
        if listOne[counter] == listTwo[counter2]:
            numberFound += 1
        elif listOne[counter] < listTwo[counter2]:
            break
    results.append(numberFound*listOne[counter])

for result in results:
    total += result

print(total)
