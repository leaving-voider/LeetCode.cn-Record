###############################################################################################
# 哈希表+遍历查找是超时的
###########
# 时间复杂度：O(n)，get中遍历查找
# 空间复杂度：O(n)，哈希表消耗
###############################################################################################
class TimeMap:

    def __init__(self):
        self.hash_ = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_[key].append(",".join([value, str(timestamp)]))

    def get(self, key: str, timestamp: int) -> str:
        get_ = self.hash_[key]
        if len(get_) == 1:
            return get_[0].split(",")[0]
        get_ = [per.split(",")[0] for per in get_ if int(per.split(",")[-1]) <= timestamp]
        return "" if len(get_) == 0 else get_[-1]


###############################################################################################
# 哈希表+二分(正好在acwing上学了)，timestamp在题目中严格递增，可以直接按数值二分
###########
# 时间复杂度：O(logn)
# 空间复杂度：O(n)
###############################################################################################
class TimeMap:
    def __init__(self):
        self.hash_ = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        get_ = self.hash_[key]
        if len(get_) == 0:
            return ""
        if len(get_) == 1:
            return get_[0][0]
        l, r = 0, len(get_)-1
        while l<r:
            mid = (l+r+1)>>1
            if get_[mid][1] <= timestamp:
                l = mid
            else:
                r = mid - 1
        return get_[l][0] if get_[l][1] <= timestamp else ""