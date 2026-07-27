class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix_mult = [1] * (size + 1)
        suffix_mult = [1] * (size + 1)

        for i in range(size):
            prefix_mult[i + 1] = nums[i] * prefix_mult[i]
        
        for i in range(size):
            suffix_mult[i + 1] = nums[size - i - 1] * suffix_mult[i]
        return [prefix_mult[i] * suffix_mult[size - i - 1] for i in range(size)]