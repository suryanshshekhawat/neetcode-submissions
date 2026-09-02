class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get distinct elements
        distinct_numbers = set(nums)

        # make a dict where you put count
        freq_dict = dict.fromkeys(distinct_numbers, 0)
        for i in range(0, len(nums)):
            freq_dict[nums[i]] += 1
        
        # now make the freq counter
        freq = list()
        for i in range(len(nums) + 1):
            freq.append(list())

        for item, value in freq_dict.items():
            freq[value].append(item)

        # filter from the back the first k modal elements !
        flat_list = []

        for row in freq:
            for item in row:
                flat_list.append(item)

        # return last k elements
        return flat_list[-1:-k-1:-1]


