class Solution(object):
    def canMeasureWater(self, x, y, z):
         def gcd(a,b):

            while b:
                a, b = b , a % b
            return a 
         if z > x + y:
            return False
         if z == 0:
            return True
        
         return z % gcd(x,y) == 0

