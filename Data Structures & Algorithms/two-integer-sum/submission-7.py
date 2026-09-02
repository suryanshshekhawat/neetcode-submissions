class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(0, len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]

        # faster solution
        
        indices = {} # value -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
        return []


        
