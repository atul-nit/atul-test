import copy

"""
shallow copy will create a new reference of outer object but will keep the same references for nested objects
"""
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
#
# old_list[1][1] = 'AA'
#
# # both the lists will change
# print("Old list:", old_list)
# print("New list:", new_list)
#
# # elements is added to only old_list
# old_list.append([10,20])
# print("\n")
# print("Old list:", old_list)
# print("New list:", new_list)
#
# # both the lists are modified
# old_list[0].append(10)
# print("\n")
# print("Old list:", old_list)
# print("New list:", new_list)


# example of deepcopy
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
# old_list[1][1] = 'AA'
# # only old_list will change
# print("Old list:", old_list)
# print("New list:", new_list)