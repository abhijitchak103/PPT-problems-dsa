"""
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""
intervals = [[0,30], [5,10], [15,20]]

def canAttendMeetings(intervals: list[list[int]]) -> bool:
    # Sort meeting times by their end times
    intervals.sort(key=lambda x: x[-1])

    # We compare whether a meeting's end time is greater than 
    # the next meeting's start time or not
    # If yees, return False,
    # Else, return True
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    
    return True

print(canAttendMeetings(intervals))