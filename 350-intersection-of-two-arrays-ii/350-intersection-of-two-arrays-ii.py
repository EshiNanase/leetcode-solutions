class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = {key:nums1.count(key) for key in nums1}
        nums2 = {key:nums2.count(key) for key in nums2}
        
        if len(nums1) > len(nums2):
            main = nums1
            second = nums2 
        else:
            main = nums2
            second = nums1
            
        answer = []
        for i in main:
            if i in second:
                for j in range(min(main[i], second[i])):
                        answer.append(i)
        return answer