import csv

# Reading a file into list
# with open("sample.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
    # print(list((csv_reader)))
    # header = next(csv_reader)
    # print(header)
    # for ele in csv_reader:
    #     print(ele)
    # csv_file.seek(0)
    # for ele in csv_reader:
    #     print(ele)

# Reading a file into dictionary
# from collections import OrderedDict
# with open("sample.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    # print(list(csv_reader))
    # for line in csv_reader:
    #     print(line)

# import csv
#
with open('employee_file.csv', mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# import csv
#
# with open('employee_file.csv', mode='w', newline='') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     data = [
#         ['John Smith', 'Accounting', 'November'],
#         ['Erica Meyers', 'IT', 'March']
#     ]
#     employee_writer.writerows(data)

# import csv
#
# with open('sample1.csv', mode='w', newline='') as s1:
#     with open('sample.csv', mode='r') as s2:
#         csv_reader = list(csv.reader(s2))
#         s1_writer = csv.writer(s1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         s1_writer.writerows(csv_reader)
