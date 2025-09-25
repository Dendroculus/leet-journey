class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorts = []
        group = {}
        for word in strs:
            sorts.append("".join(sorted(word)))
            
        for i, j in zip(strs, sorts):
            if j not in group:
                group[j] = [i]
            else :
                group[j].append(i)

        return list(group.values())

            

