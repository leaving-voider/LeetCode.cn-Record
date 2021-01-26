class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ################## 这种直接超时
        # for i in range(length):
        #     for j in range(i+1, length):
        #         if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]):
        #             num += 1

        ################## 一次遍历，速度不错，但使用字典，内存消耗大
        num = 0
        length = len(dominoes)
        dict_ = {}
        
        cur = 0
        rev = 0
        # 这种方法主要抓住牌对的本质，我们只需要把同一个牌对的排放一起，用字典记录等价牌个数
        for per in dominoes:
            cur = tuple(per)
            rev = (per[1], per[0])
            if cur in dict_:
                dict_[cur] += 1
            elif rev in dict_:
                dict_[rev] += 1
            else:
                dict_[cur] = 1
        # 因为牌对为(i,j)且i<j，i和j为某牌在序列中的下标，说明这是考虑顺序的
        # 1个等价牌：牌对为0，2个等价牌：牌对为1，3个等价牌：牌对为3。规律即n*(n-1)/2
        # 最后统计即可
        for per in dict_:
            cur = dict_[per]*(dict_[per]-1)//2
            num += cur
        return num
