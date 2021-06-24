###############################################################################################
# 自己使用哈希强行解，需要注意的点是：
# （1）使用k和b来作为唯一标识
# （2）当直线为垂直时，b为None，斜率k需要加入x轴位置来作为唯一标识
###########
# 时间复杂度：O(n^2), 两个循环遍历所有边
# 空间复杂度：O(n^2)，最坏可能每两个点的斜率和b的组合都不一样
###############################################################################################
class Solution:
    def maxPoints(self, points) -> int:
        pointsNum = len(points)
        de = defaultdict(list)
        for i in range(pointsNum):
            for j in range(i+1, pointsNum):
                deltaX = points[i][0] - points[j][0]
                k = (points[i][1] - points[j][1])/deltaX if deltaX != 0 else f"{float('inf')}{points[j][0]}"
                b = points[i][1] - k*points[i][0] if type(k) != str else None
                if str(points[i]) not in de[(k, b)]:
                    de[(k, b)].append(str(points[i]))
                if str(points[j]) not in de[(k, b)]:
                    de[(k, b)].append(str(points[j]))
        max_ = 1
        for per in de:
            max_ = max(len(de[per]), max_)
        return max_	

###############################################################################################
# 官方方法，利用了一定的剪枝
###########
# 时间复杂度：O((n^2)*logm), 其中 n 为点的数量，m 为横纵坐标差的最大值, 最坏情况下我们需要枚举所有 n 个点
## 枚举单个点过程中需要进行 O(n) 次最大公约数计算，单次最大公约数计算的时间复杂度是 O(logm)，
# 空间复杂度：O(n)，主要为哈希表的开销
###############################################################################################
class Solution:
    def gcd(self, a, b):
        return self.gcd(b, a % b) if b else a # 直到b为0就返回a，即最大公约数

    def maxPoints(self, points) -> int:
        n = len(points)
        if n <= 2: # 当点少于等于2（剪枝一）
            return n # 直接返回，必定同一直线
        ret = 0 # 记录最大可能的在同一直线的点数
        for i in range(n):
            # 当之前的最多点都已经大于剩下的点，或过半了，则不用再查了（剪枝三，剪枝四）
            if ret >= n - i or ret > n / 2: 
                break
            mp = defaultdict(int) # 只需要保存i及之后的点的斜率，从而避免斜率同b不同的情况（剪枝二）
            for j in range(i + 1, n):
                x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
                if x == 0:
                    y = 1
                elif y == 0:
                    x = 1
                else:
                    x, y = (-x, -y) if y < 0 else (x, y)
                    gcdXY = self.gcd(abs(x), abs(y))
                    x /= gcdXY
                    y /= gcdXY
                
                mp[y + x * 20001] += 1 # 保证每个斜率k映射到的值不同, 比如1/2 和 2/1， 直接加起来都是3
            ret = max(ret, max([mp[per] + 1 for per in mp]))
        return ret