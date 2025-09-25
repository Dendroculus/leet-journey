class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
            
        right = 1
        for i in range(n-1, -1, -1): 
            answer[i] *= right
            right *= nums[i]
            
        return answer
        
        
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
'''
0 | answer[0] = 1, 1 *= 1, answer = [1,1,1,1], left = 1
1 | answer[1] = 1, 1 *= 2, answer = [1,1,1,1], left = 2
2 | answer[2] = 1, 2 *= 3, answer = [1,1,2,1], left = 6
3 | answer[3] = 1, 6 *= 4, answer = [1,1,2,6], left = 24

3 | answer[3]*1 = 6, answer = [1,1,2,6], right = 4
2 | answer[2]*4 = 8, answer = [1,1,8,6], right = 12
1 | answer[1]*12 = 12, answer = [1,12,8,6], right = 24
0 | answer[0]*24 = 24, answer = [24,12,8,6], right =24
'''