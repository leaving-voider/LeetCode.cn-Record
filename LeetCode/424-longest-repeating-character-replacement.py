#####################################################################################
# 整个基于双指针的算法的解题逻辑是，记录下历史上拥有最大重复字母且其余字母之和不大于k的区间
# 当然记录这个区间的方式只是记录了那个最大重复字母的数量，毕竟原题不需要我们提供两个端点
# 而且在找到答案要求的最大后，即便再往后移动，如果不能找到重复字母更大的区间，即maxnum不增加
# right - left + 1 - maxnum会一直大于k，left会一直伴随right同时加1，因此区间大小不变
# 最后根据题目要求，返回替换后的最长子串长度，也就是当前区间的长度
#####################################################################################
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 左右双指针 ＋ 记录历史上某个区间里出现次数最大的字母的数量
        left = right = maxnum = 0
        # 记录当前区间，26个字母各自的个数, 初始化为0
        letters = [0]*26
        # 字符串总长度
        length = len(s)

        for per in s:
            # 当前字母id，ord函数返回对应的 ASCII 数值
            id_ = ord(per) - ord("A")
            # 当前字母个数+1
            letters[id_] += 1
            # 更新历史最大
            maxnum = max(maxnum, letters[id_])
            # 如果当前区间长度 - 历史单个字母最大数量 > k，只能left往右移1个
            if right - left + 1 - maxnum > k:
                # left对应字母数量 -1
                letters[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left