from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}_{s}" for s in strs)
    
    def decode(self, s: str) -> List[str]:
        lt= []
        i = 0
        while i < len(s):
                j = i
                while s[j] != "_":
                    j +=1
                length = int(s[i:j])
                word = s[j+1 : j+1+length]
                lt.append(word)
                i = j + 1 + length
        return lt
    
    
sol = Solution()
encoded = sol.encode(["neet", "code", "love", "you"])
print(encoded)            
print(sol.decode(encoded))