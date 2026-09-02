class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This solution is O(n^2)
        #for i in range(0, len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]

        # We can do better, we can get O(n)
            seen = {} # index : difference_to_target

            for index, number in enumerate(nums):

                difference = target - number

                if difference in seen:
                    return [seen[difference], index]

                seen[number] = index


            
