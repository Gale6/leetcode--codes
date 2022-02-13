from lib2to3.pgen2.pgen import DFAState
import re
from traceback import print_tb


def longestConsecutiveSequence(nums):
    numset = set(nums)
    longest = 0
    print(numset)
    for n in nums:
        if n-1 not in numset:
            currLongest = 1
            while (n+currLongest) in numset:
                currLongest += 1
            longest = max(longest,currLongest)
    return longest







nums =[100,4,200,1,3,2]
print(longestConsecutiveSequence(nums))