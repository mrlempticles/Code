class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")


        max_len = max(len(v1), len(v2))
        v1 += ['0'] * (max_len - len(v1))
        v2 += ['0'] * (max_len - len(v2))

        for i in range (max_len):
            num1 = int(v1[i])
            num2 = int(v2[i])

            if num1 > num2:
                 return 1
            elif num1 < num2:
                 return -1 

        return 0