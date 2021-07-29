# # import random
# # import pygame
# # __author__ = 'Noah Vendrig'
# # __license__ = 'MIT'  # copy of the license available @ https://prodicus.mit-license.org/
# # __version__ = '1.0.1'
# # __email__ = 'noah.vendrig@education.nsw.gov.au'
# # __github__ = "github.com/noahvendrig"  # @noahvendrig
# # __course__ = 'Software Design and Development'
# # __date__ = '10/07/2021'
# # __description__ = 'Modern Recreation of text-based adventure game Hunt the Wumpus (1973)'
# # __specifications__ = "noahvendrig.com/#about"  # specifications available here

# # print('# ' + '=' * 78)
# # print('Author: ' + __author__)
# # print('License: ' + __license__)
# # print('Version: ' + __version__)
# # print('Email: ' + __email__)
# # print('Course: ' + __course__)
# # print('Date: ' + __date__)
# # print('Description: ' + __description__)
# # print('# ' + '=' * 78)


# # ########################################################################################################################
# graph = {
#         1: [2, 5, 8],
#         2: [10, 3, 1],
#         3: [2, 4, 12],
#         4: [3, 5, 14],
#         5: [1, 4, 6],
#         6: [5, 7, 15],
#         7: [6, 8, 17],
#         8: [1, 7, 9],
#         9: [8, 10, 18],
#         10: [11, 9, 2],
#         11: [10, 12, 19],
#         12: [3, 11, 13],
#         13: [12, 14, 20],
#         14: [4, 13, 20],
#         15: [6, 14, 16],
#         16: [15, 17, 20],
#         17: [7, 16, 18],
#         18: [9, 17, 19],
#         19: [11, 18, 20],
#         20: [13, 16, 19],
#     }
# from itertools import permutations

# num = 3
# all_nums = []
# all_combs = []

# for i in range(1, num+1):
#     all_nums.append(i)

# comb = permutations(all_nums, 3)


# # print(sum(1 for _ in comb))


# dict = {}
# n = 0

# comb_list = [c for c in comb]
# big = permutations(comb_list, num)
# # big_list = [b for b in big]
# big_list = []
# counter = 0
# for b in big:
#     counter += 1
#     big_list.append(b)
# print(big_list)

# # print(big_list)
# print("finished")
# # for i in big_list:
# #     print(list(i))
# # for i in big:
# #     n +=1
# #     if n<= num:
# #         print("GUCCI")
# #         elements = list(i)
# #         dict[n] = elements
# #     else:
# #         break

# # print(dict)


# ####################

# from pixellator import Pixellate

# pixellatedImg = Pixellate("./img/bats.png", 100)
