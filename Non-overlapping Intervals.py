from cgi import print_directory


def eraseOverlapIntervals(intervals):
    intervals.sort()

    res=0
    preEnd = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= preEnd:
            preEnd = end
        else:
            preEnd = min(preEnd,end)
            res+=1
    return res



print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))