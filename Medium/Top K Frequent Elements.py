class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sorted(freq.keys(), key=freq.get, reverse=True)[:k]