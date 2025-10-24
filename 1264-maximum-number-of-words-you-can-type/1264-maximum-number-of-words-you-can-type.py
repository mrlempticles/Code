class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        print(text)
        print(brokenLetters)
        count = 0 
        words = text.split()

        for word in words:
            if not any(b in word for b in brokenLetters):
              count += 1
              
        print(count)
        return(count)