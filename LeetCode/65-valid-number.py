###############################################################################################
# 此题一眼就看出是属于编译原理的内容，凭借当年强大的编译原理实验的功底，强行将此题写出来通过了
# 不过缺点是太冗余了，很多操作太傻，还是需要编译理论的知识进行规范编程
###########
# 时间复杂度：O(n)，n为字符串长度
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def isNumber(self, s: str) -> bool:
        self.i = 0
        self.len_ = len(s)
        def part1(ch, s):
            if ch == '+' or ch == '-':
                self.i += 1
                if self.i >= self.len_:
                    return False
                ch = s[self.i]
            if ch >= '0' and ch <= '9':
                self.i += 1
                if self.i >= self.len_:
                    return True
                ch = s[self.i]
                while ch >= '0' and ch <= '9':
                    self.i += 1
                    if self.i >= self.len_:
                        return True
                    ch = s[self.i]
                if ch == '.':
                    self.i += 1
                    if self.i >= self.len_:
                        return True
                    ch = s[self.i]
                    while ch >= '0' and ch <= '9':
                        self.i += 1
                        if self.i >= self.len_:
                            return True
                        ch = s[self.i]
            elif ch == '.':
                self.i += 1
                if self.i >= self.len_:
                    return False
                ch = s[self.i]
                if ch >= '0' and ch <= '9':
                    while ch >= '0' and ch <= '9':
                        self.i += 1
                        if self.i >= self.len_:
                            return True
                        ch = s[self.i]
                else:
                    return False
            else:
                return False
            return True
        def part2(ch, s):
            if ch == 'e' or ch == 'E':
                self.i += 1
                if self.i >= self.len_:
                    return False
                ch = s[self.i]
                if ch == '+' or ch == '-':
                    self.i += 1
                    if self.i >= self.len_:
                        return False
                    ch = s[self.i]
                if ch >= '0' and ch <= '9':
                    while ch >= '0' and ch <= '9':
                        self.i += 1
                        if self.i >= self.len_:
                            return True
                        ch = s[self.i]
                else:
                    return False
            return False
        if not part1(s[self.i], s):
            return False
        if self.i < self.len_:
            if not part2(s[self.i], s):
                return False
        return True



###############################################################################################
# 显然官方使用的自动机能够以非常规范的方式进行编程，但在python里似乎效率并不高，估计是使用了Enum库的原因
###########
# 时间复杂度：O(n)，n为字符串长度
# 空间复杂度：O(1)
###############################################################################################
from enum import Enum

class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END"
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_ILLEGAL"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            else:
                return Chartype.CHAR_ILLEGAL
        
        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]
        # 如下状态都是可以直接到State.STATE_END状态的合法状态
        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER]