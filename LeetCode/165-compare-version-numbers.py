###############################################################################################
# 确实简单
###########
# 时间复杂度：O(n)，n表示以‘.’分开后的数组长度
# 空间复杂度：O(m)，m表示两个字符串长度
###############################################################################################
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        len_v1, len_v2 = len(version1), len(version2)
        if len_v1 < len_v2:
            version1.extend(['0']*(len_v2 - len_v1))
        else:
            version2.extend(['0']*(len_v1 - len_v2))
        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
        return 0