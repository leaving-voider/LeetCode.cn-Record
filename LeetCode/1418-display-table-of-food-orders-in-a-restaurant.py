###############################################################################################
# 题目简单，就是麻烦，使用哈希表解决问题
###########
# 时间复杂度：O(T + NlogN + MlogM + MN), 其中 T 是数组 orders 的长度，N 是数据表的列数（即餐品的数量），M 是数据表的行数（即餐桌的数量）
### 遍历一次orders（T） + 对餐品名字排个序（NlogN） + 对餐桌号排个序（MlogM） + 逐行填表
# 空间复杂度：O(T + M + N), 只计算额外的空间复杂度
###############################################################################################
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        lists = defaultdict(lambda: defaultdict(int)) # 对嵌套defaultdict内层进行指定类型的写法
        menuNames = set()
        tableNumbers = set()
        for _, tableNumber, foodItem in orders:
            lists[tableNumber][foodItem] += 1
            menuNames.add(foodItem)
            tableNumbers.add(tableNumber)
        menuNames = list(menuNames)
        menuNames.sort() # 菜品名字排序
        res = []
        for num in sorted(list(tableNumbers), key=lambda x: int(x)): # 排序后，遍历每一桌
            res.append([num])
            for i in range(len(menuNames)):
                res[-1].append(str(lists[str(num)][menuNames[i]]))
        return [["Table"] + menuNames] + res