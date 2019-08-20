import csv

data = [{'mountain' : 'Everest', 'height': '8848'},
      {'mountain' : 'K2 ', 'height': '8611'},
      {'mountain' : 'Kanchenjunga', 'height': '8586'}]
with open('peak1.csv', 'w') as csvFile:
    fields = ['height', 'mountain']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)