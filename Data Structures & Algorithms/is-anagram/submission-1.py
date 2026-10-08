class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sDict={}
            tDict={}
            for n in range(len(s)):
                sDict[s[n]] = (sDict.get(s[n]) or 0) + 1
                tDict[t[n]] = (tDict.get(t[n]) or 0) + 1
            for char in sDict.keys():
                if sDict[char] != tDict.get(char,0):
                    return False

            return True
