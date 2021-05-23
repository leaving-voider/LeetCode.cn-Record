###############################################################################################
# 前缀树Trie，也叫字典树，一种树形数据结构。用于高效地存储和检索字符串数据集中的键。
# 这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
###########
# 时间复杂度：初始化为 O(1)，其余操作为 O(|S|)，其中 |S|是每次插入或查询的字符串的长度
# 空间复杂度：O(∣T∣⋅Σ)，其中 |T| 为所有插入字符串的长度之和，Σ 为字符集的大小，本题 Σ=26；
# 每个节点都有一个长度26的children，而节点个数最坏情况下，所有插入字符串都没有公共前缀，每个字母都开辟了自己的children
# 因此空间复杂度最坏为O(∣T∣⋅Σ)
###############################################################################################
class Trie:
    def __init__(self):
        self.children = [None]*26 # 26个小写字母
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a") # 计算在self.children的位置
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def searchPrefix(self, word:str):
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None