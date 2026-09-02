class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1)
        frequent = set(nums) # this is a collection of unique elements within the list

        # O(1)
        # make a dictionary with 0s as values and set elements as keys
        dictionary = dict.fromkeys(frequent, 0)

        # O(n)
        # go through list and update values
        for i in range(0, len(nums)):
            dictionary[nums[i]] += 1

        # O(n log n)
        # sort and pick the first k !
        sorted_dict = dict(sorted(dictionary.items(), key = lambda x: x[1], reverse=True))
        
        # O(n)
        # get the first k elements from the dictionary
        result = []
        count = 0

        for key, value in sorted_dict.items():
            if count == k:
                break
            else:
                result.append(key)
                count += 1

        # return list
        return result