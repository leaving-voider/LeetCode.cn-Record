###############################################################################################
# 此题关键：可采用哈希映射来存放家族树，得到继承顺序使用递归即可
###########
# 时间复杂度：初始化、出生、死亡都可视为O(1)，得到继承顺序遍历一次树，为 O(n)
# 空间复杂度：存放树、存死亡人、以及递归的栈空间消耗都为 O(n)
# 上述的时空复杂度分析中，我们默认了所有字符串（即人名）的操作时间以及存储空间都是 O(1) 的
###############################################################################################
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.trees = defaultdict(list) # 哈希映射存树，默认值为空列表
        self.deads = set() # 死亡人名单
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.trees[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        
        def getOrder(Name):
            if Name not in self.deads:
                ans.append(Name)
            for perChild in self.trees[Name]:
                getOrder(perChild)
        
        getOrder(self.kingName)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()