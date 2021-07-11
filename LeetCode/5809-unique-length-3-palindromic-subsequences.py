class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hash_, res = defaultdict(list), 0
        for i in range(len(s)):
            hash_[s[i]].append(i)
        for letter in range(97, 97+26):
            if chr(letter) in hash_ and len(hash_[chr(letter)]) > 1:
                res += len(set(s[hash_[chr(letter)][0]+1:hash_[chr(letter)][-1]]))
        return res