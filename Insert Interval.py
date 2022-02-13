def insert(intervals,newInterval):

    res = []

    for i in range(len(intervals)):
        if intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        elif intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
    res.append(newInterval)

    return res








#print(insert([[1,5]],[2,3]))
#print(insert([[1,3],[6,9]],[2,5]))

#print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(insert([[1,5]],[2,7]))