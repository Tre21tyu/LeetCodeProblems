# Loop through each unique element 
# For each element
#     Create a key with a value of 0
#         Loop through linked list
#             if there is a from
#                 make that value from
# return key with value that = 0
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# [expression for item in iterable if condition]
# newlist = [x for x in fruits if "a" in x]
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        len_path = len(paths)
        # new_dict = {element:'Tue' for element in list_keys}
        cities_dict = { _: '0' for _ in set([path for city in paths for path in city]) }
        return cities_dict
# paths[0][0] paths[0][1] paths[1][0] paths[1][1] paths[2][0] paths[2][1]
# New York
# Lima
# Sao Paulo
# London
# [{ "New York" : 0 },{ "Lima" : 0 },{ "Sao Paulo" : 0 },{ "London" : 0 }]
solution = Solution()
paths = [["New York","Lima"],["Lima","Sao Paulo"],["London","New York"]]
# 
paths2 = [["B","C"],["D","B"],["C","A"]]

print(solution.destCity(paths))
# print(solution.destCity(paths2))
