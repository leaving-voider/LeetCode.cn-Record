###############################################################################################
# 遍历一遍
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        list_s = list(s)
        while i < j:
            while i < j and list_s[i] not in vowels:
                i += 1
            while i < j and list_s[j] not in vowels:
                j -= 1
            if i < j:
                list_s[i], list_s[j] = list_s[j], list_s[i]
                i += 1
                j -= 1
        return ''.join(list_s)