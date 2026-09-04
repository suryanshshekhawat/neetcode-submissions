class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = set(nums) # this is a collection of unique elements within the list

        # make a dictionary with 0s as values and set elements as keys
        dictionary = dict.fromkeys(frequent, 0)

        # go through list and update values
        for i in range(0, len(nums)):
            dictionary[nums[i]] += 1

        # filter dictionary and append value to list 
        result = []
        for key, value in dictionary.items():
            if value >= k:
                result.append(key)

        # return list
        return result