class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = end - (end - start) // 2
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid

        if start == len(nums) -1:
            return nums[0]
        elif nums[start] > nums[start + 1]:
            return nums[start + 1]
        elif end == len(nums) - 1:
            return nums[0]
        elif nums[end] > nums[end + 1]:
            return nums[end + 1]
      
        
