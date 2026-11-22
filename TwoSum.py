class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in checked:
                return [checked[complement], i]
            
            checked[num] = i
        return []    
