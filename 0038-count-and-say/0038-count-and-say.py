class Solution(object):
    def countAndSay(self, n):
        s = "1"
        
        for _ in range(n - 1):
            new_s = ""
            i = 0
            
            while i < len(s):
                count = 1
                # Count same consecutive characters
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                
                new_s += str(count) + s[i]
                i += 1
            
            s = new_s
        
        return s
