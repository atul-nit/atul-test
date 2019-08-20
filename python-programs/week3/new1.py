import csv
import operator

# with open("sysd.txt", 'r') as f:
#     content = f.read()
#     lines = content.split(" ")
#     print(lines)
#     print(len(lines))

with open("212_steelos_new_feature.csv", 'r') as fr:
    reader = csv.reader(fr, delimiter=",")
    sortedlist = sorted(reader, key=operator.itemgetter(1))
    print(sortedlist)
    with open('sorted_212.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(sortedlist)
