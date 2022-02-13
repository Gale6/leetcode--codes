def merge(intervals):
    res = []
    intervals.sort()
    for i in intervals:
        if len(res) == 0:
            res.append(i)
        else:
            if res[len(res)-1][1] >= i[0]:
                res[len(res)-1] = [min(res[len(res)-1][0],i[0]),max(res[len(res)-1][1],i[1])]
            else:
                res.append(i)
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))