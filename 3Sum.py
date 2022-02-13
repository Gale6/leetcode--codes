def threeSum(nums):
    output = []
    sortedNum = sorted(nums)
    for i in range(len(sortedNum)):
        if i > 0 and sortedNum[i] == sortedNum[i-1]:
            continue
        L = i+1
        R = len(sortedNum) -1
        while L < R:
            if sortedNum[L] + sortedNum[R] < 0 - sortedNum[i]:
                L = L +1
            elif sortedNum[L] + sortedNum[R] > 0 - sortedNum[i]:
                R = R -1
            else:    
                output.append([sortedNum[i],sortedNum[L],sortedNum[R]])
                L = L +1
                R = R -1
                while sortedNum[L] == sortedNum[L-1] and L<R:
                    L += 1
    return output


print(threeSum([-1,0,1,2,-1,-4]))



