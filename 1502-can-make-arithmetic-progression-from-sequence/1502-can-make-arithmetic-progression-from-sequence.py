class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for ind, num in enumerate(arr[:-1]):
            print(arr[ind] - arr[ind-1])
            if arr[ind+1] - arr[ind] != diff:
                return False
        return True