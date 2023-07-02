class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisons = 0
        for time_ind, time in enumerate(timeSeries):
            try:
                if time + duration < timeSeries[time_ind+1]: 
                    poisons += duration
                else:
                    difference = timeSeries[time_ind+1] - timeSeries[time_ind]
                    poisons += difference
            except:
                poisons += duration
        return poisons