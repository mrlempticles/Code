class Solution(object):
    def findLexSmallestString(self, s, a, b):
        from collections import deque
        
        seen = set()
        q = deque([s])
        smallest = s
        
        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            
            if cur < smallest:
                smallest = cur
            
            # Operation 1: add to odd indices
            add_str = list(cur)
            for i in range(1, len(cur), 2):
                add_str[i] = str((int(add_str[i]) + a) % 10)
            add_str = ''.join(add_str)
            
            # Operation 2: rotate
            rot_str = cur[-b:] + cur[:-b]
            
            # push both to queue
            q.append(add_str)
            q.append(rot_str)
        
        return smallest
