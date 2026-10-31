"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        counts = 0
        i,j = 0,0
        while i < len(starts):
            if starts[i] >= ends[j]:
                counts -= 1
                j += 1
            else:
                counts += 1
                i += 1
            res = max(res, counts)
        
        return res

