def isAnagram(s, t):
    if len(s) != len(t):
        return False
    oriSet = {}
    for char in s:
        oriSet[char] = oriSet.get(char, 0) + 1
    targetSet = {}
    for char in t:
        targetSet[char] = targetSet.get(char, 0) + 1
    for char in oriSet:
        if oriSet.get(char) != targetSet.get(char, 0):
            return False
    return True
