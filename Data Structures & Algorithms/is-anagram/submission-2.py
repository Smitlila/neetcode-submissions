class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #Dictionry/hashmap for storing the count of all letters as a key 
        # value pair
        countS, countT = {}, {}

        for i in range(len(s)):
            #get method to have the key and the count with default 0 if not
            #in dictionary
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
        