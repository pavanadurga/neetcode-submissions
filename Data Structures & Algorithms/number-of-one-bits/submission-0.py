class Solution:
    def hammingWeight(self, n: int) -> int:
        s=""
        while n > 0:
            if n%2 == 0:
                s+="0"
            else:
                s+="1"
            n=n//2
        return s.count("1")
