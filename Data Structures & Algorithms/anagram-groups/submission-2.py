class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in pairs:
                pairs[key] = [word]
            else:
                pairs[key].append(word)
        answerArray = []
        for key in pairs.values():
            answerArray.append(key)

      

        return answerArray