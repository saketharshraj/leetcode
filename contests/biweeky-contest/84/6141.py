# https://leetcode.com/contest/biweekly-contest-84/problems/merge-similar-items/

# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

# items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
# The value of each item in items is unique.
# Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

# Note: ret should be returned in ascending order by value.

 

# Example 1:

# Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]
# Explanation: 
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
# The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
# The item with value = 4 occurs in items1 with weight = 5, total weight = 5.  
# Therefore, we return [[1,6],[3,9],[4,5]].

from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i in items1:
            d[i[0]] = i[1]
        
        for i in items2:
            if i[0] in d:
                d[i[0]] += i[1]
            else:
                d[i[0]] = i[1]

        return sorted(d.items(), key=lambda x: x[0])

s = Solution()
print(s.mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))