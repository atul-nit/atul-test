import csv

# l1 = []
# with open("nnn.csv", 'r') as fr:
#     csv_reader = csv.reader(fr, delimiter=',')
#     for line in fr:
#         if "troubleshoot" in line:
#
#             l1.append(str(line).strip('"\n'))
# print(len(l1))
#
#
#
# s = " ".join(l1)
# print(s)
# with open("new_feature2.txt", "w") as fw:
#     fw.write(s)

# l1 = []
# with open("nnn.csv", 'r') as fr:
#     csv_reader = csv.reader(fr, delimiter=',')
#     for line in fr:
#         if "test_cli" in line or "test_ctrl_c_on_cli" in line or "multiple_cli" in line or "test_tcpdump" in line:
#             l1.append(str(line).strip('"\n'))
# print(len(l1))
#
# s = " ".join(l1)
# print(s)
# with open("new_feature3.txt", "w") as fw:
#     fw.write(s)


# with open("sysd.txt", 'r') as f:
#     content = f.read()
#     lines = content.split(" ")
#     print(lines)
#     print(len(lines))

# with open("rsys.txt", 'r') as f:
#     content = f.read()
#     lines = content.split(" ")
#     print(lines)
#     print(len(lines))


with open("steelos_infrastructure.csv", 'r') as fr:
    p1_str = ''
    p2_str = ''
    p3_str = ''
    csv_reader = csv.reader(fr, delimiter=',')
    l1 = list(csv_reader)
    for line in l1:
        if "P1" in line[1]:
            # if ".py" in line[0]:
                p1_str += line[0] + "\n"
        elif "P2" in line[1]:
            p2_str += line[0] + "\n"
        elif "P3" in line[1]:
            p3_str += line[0] + "\n"
        else:
            continue

    with open("catfish_p1.txt", "w") as f:
        f.write(p1_str)

    with open("catfish_p2.txt", "w") as f:
        f.write(p2_str)

    with open("catfish_p3.txt", "w") as f:
        f.write(p3_str)


# with open("steelos_infrastructure_panther.csv", 'r') as fr:
#     p1_str = ''
#     p2_str = ''
#     csv_reader = csv.reader(fr, delimiter=',')
#     l1 = list(csv_reader)
#     for line in l1:
#         if "P1" in line[1]:
#             # if ".py" in line[0]:
#                 p1_str += line[0] + "\n"
#         elif "P2" in line[1]:
#             # if ".py" in line[0]:
#                 p2_str += line[0] + "\n"
#         else:
#             continue
#
#     with open("panther_p1.txt", "w") as f:
#         f.write(p1_str)
#
#     with open("panther_p2.txt", "w") as f:
#         f.write(p2_str)
