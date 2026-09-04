class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(0, len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]

        # faster solution
        
        differences = {}

        for i in range(0, len(nums)):
            differences.update({i:target - nums[i]})

        for j in range(0, len(nums)):
            if j in differences.values():
                return [index(j), j]
        
