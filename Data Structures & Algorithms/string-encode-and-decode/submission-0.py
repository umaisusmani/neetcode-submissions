class Solution:
    def encode(self, strs: List[str]) -> str:
        length=len(strs)
        delimeter = "#_"
        enc=""
        for word in strs:
            enc+= delimeter + word
        eVal=delimeter + str(length) + enc
        print(eVal)
        return eVal
            

    def decode(self, s: str) -> List[str]:
        dVal=[]
        startIndex= s.find("#_")
        fullSplit = s[startIndex:].split("#_")
        length= int(fullSplit[1])
        dVal=fullSplit[2:2+length]
        print(dVal)
        return dVal
        
            