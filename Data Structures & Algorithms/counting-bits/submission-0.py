class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            p=''
            j=i
            while j >0:
                if j%2 == 0:
                    p+="0"
                else:
                    p+="1"
                j=j//2
            ans.append(p.count("1"))
        return ans