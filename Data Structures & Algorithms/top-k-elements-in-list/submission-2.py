class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = set(nums) # this is a set

        result = []

        counter = 0
        for i in frequent:
            counter = self.countOccurence(i, nums)
            if counter >= k:
                result.append(i)
            counter = 0

        return result
        
    # helper function
    def countOccurence(self, n: int, numbers: List[int]) -> int:
        count = 0
        for i in range(0, len(numbers)):
            if n == numbers[i]:
                count += 1
        return count