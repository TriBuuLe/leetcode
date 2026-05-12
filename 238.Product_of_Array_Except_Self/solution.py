class Solution:
    def productExceptSelf(self, nums):
        '''
        [1,2,3,4]
        [24,12,4,1]
        [24,12,8,6]
        '''
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        # answer: [1,1,2,6]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        # answer: [24,12,8,6]
        return answer

