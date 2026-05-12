class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        '''
        answer = [1,1,1,1]
        nums = [2,3,4,5]

        prefix = 1
        i = 0 -> answer: [1,1,1,1] prefix = 2
        i = 1 -> answer: [1,2,1,1] prefix = 6
        '''
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
        


