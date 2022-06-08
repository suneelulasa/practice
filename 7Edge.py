# def sort_by_frequency(arr):
#     res,l1, l2 = {}, [], []
#     for i in arr:
#         res[i] = arr.count(i)
#     [l1.append(str(i) * j) for i, j in res.items()]
#     [l2.extend(list(i)) for i in sorted(l1, key=len, reverse=True)]
#     return [int(i) for i in l2]
# print(sort_by_frequency([0, 1, 8, 1, 7, 1, 9, 1, 2, 2, 6, 2, 6, 0, 1, 2, 3, 5, 1]))
#
# # taking the function to find out the frequency
# def sort_by_frequency(arr):
#     res,l1, l2 = dict(), [], []
#   # considered empty dictionary and two empty lists
#     for i in arr:
#         res[i] = arr.count(i) # updated dictionary with each value as key and its count as value
#     [l1.append(str(i) * j) for i, j in res.items()] # converted into list by multiplying each key with its count, changed key from int to string type before multiplication
#     [l2.extend(list(i)) for i in sorted(l1, key=len, reverse=True)] # extended each element in list as a single value after sorting the list according to length of total character.
#     return [int(i) for i in l2] # converted back each element into int.
# print(sort_by_frequency([0, 1, 8, 1, 7, 1, 9, 1, 2, 2, 6, 2, 6, 0, 1, 2, 3, 5, 1]))


