###############################################################################################
# 依次遍历所有字符，如果是字母，则将res中的所有字符串的该位置的字母大小写进行转换
# 并作为新串加入，最后产生所有种类，随着res长度的增加，第二层循环的时间开销会越大
###########
# 时间复杂度：O(n*2的n次方)，n为字符串数的长度，2的n次方为最坏情况的第二循环的时间开销
# 空间复杂度：O(2的n次方)，比官方给的答案开销小
###############################################################################################
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        for i in range(len(S)):
            if S[i].isalpha():
                if S[i].isupper():
                    for j in range(len(res)):
                        res.append(res[j][:i] + res[j][i].lower() + res[j][i+1:])
                if S[i].islower():
                    for j in range(len(res)):
                        res.append(res[j][:i] + res[j][i].upper() + res[j][i+1:])
        return res