class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # aim: find sequence
        # idea: find start
        # plan: start -> anything where start - 1 doesnt exist

        nums_set = set(nums)
        count, max_count = 0, 0
        for num in nums:
            if num - 1 not in nums_set:
                temp = num
                while temp in nums_set:
                    count += 1
                    temp += 1
                max_count = max(max_count, count)
                count = 0
        return max_count