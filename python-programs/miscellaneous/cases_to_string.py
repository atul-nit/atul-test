import csv

feature = 'sysdump'

with open("p3_212_1_test_run.csv", 'r') as fr:
    csv_reader = csv.reader(fr, delimiter=',')
    cases = list(csv_reader)
    test_string = ''
    print(len(cases))
    for case in cases:
        if "#" in case[0]:
            continue
        test_string += case[0]+" "

    with open("teststring.txt", "w") as fw:
        fw.write(test_string)



# with open("p3_212_1_test_run.csv", 'r') as fr:
#     csv_reader = csv.reader(fr, delimiter=',')
#     cases = list(csv_reader)
#     test_string = ''
#     print(len(cases))
#     c = 0
#     for case in cases:
#         if "#" in case[0]:
#             continue
#         if feature+".py" in case[0]:
#             test_string += case[0] + " "
#             c += 1
#
#     print("test cases selected:", c)
#     with open("teststring1.txt", "w") as fw:
#         fw.write(test_string)

# with open("rsys_cat_p2.csv", 'r') as fr:
#     csv_reader = csv.reader(fr, delimiter=',')
#     cases = list(csv_reader)
#     test_string = ''
#     print(len(cases))
#     c = 0
#     for case in cases:
#         test_string += case[0] + " "
#         c += 1
#
#     print("test cases selected:", c)
#     with open("rsyslog_str_p2.txt", "w") as fw:
#         fw.write(test_string)

# with open("auto_steelos_regression_212_1.csv", 'r') as fr:
#     csv_reader = csv.reader(fr, delimiter=',')
#     cases = list(csv_reader)
#     test_string = ''
#     print(len(cases))
#     cp1 = 0
#     cp2 = 0
#     cp3 = 0
#     p1_str = ''
#     for case in cases:
#         if 'P1' in case[1]:
#             p1_str += case[0]+","+case[1]+" "
#             cp1 += 1
#         elif 'P2' in case[1]:
#             print(case)
#             cp2 += 1
#         elif 'P3' in case[1]:
#             cp3 += 1
#
#
#     print("P1 count:", cp1)
#     print("P2 count:", cp2)
#     print("P3 count:", cp3)
#     print("total:", cp1+cp2+cp3)
#     print(p1_str)

# with open("teststring1.txt", "r") as fp:
#     lines = fp.readlines()
#     lines.reverse()
#     for line in lines:
#         print(line)



