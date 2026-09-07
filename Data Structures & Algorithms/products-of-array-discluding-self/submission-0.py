class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # check if list has 0
        does_list_have_0 = False
        more_than_1_0 = False
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if does_list_have_0:
                    more_than_1_0 = True
                does_list_have_0 = True
            if more_than_1_0:
                break
        
        # calculate product without 0s ?
        full_product = 1
        for i in range(0, len(nums)):
            if nums[i] != 0:
                full_product *= nums[i]
            
        # calculate and add to list,
        result_list = [0] * len(nums)

        for i in range(0, len(nums)):
            if nums[i] != 0:
                # is not 0
                    # if there are more 0s
                    # return 0
                    if does_list_have_0:
                        result_list[i] = 0
                    # if there are not 
                    # return full product with division
                    else:
                        result_list[i] = int(full_product / nums[i])
            else:
                # is 0
                    # if there are more 0s
                    # return 0
                    if more_than_1_0:
                        result_list[i] = 0
                    # if there are no more 0s 
                    # return actual product
                    else:
                        result_list[i] = full_product

        return result_list