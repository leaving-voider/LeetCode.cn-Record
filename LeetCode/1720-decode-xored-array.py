###############################################################################################
# 采用官方方法，利用XOR的性质，可以证明arr[i]=arr[i−1]⊕encoded[i−1]
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)，官方说 空间复杂度不考虑返回值，因此为O(1)
###############################################################################################
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(res[i]^encoded[i])
        return res