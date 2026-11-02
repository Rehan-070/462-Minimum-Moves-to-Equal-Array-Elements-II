class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        s=sorted(nums)
        l=len(nums)
        m=s[l//2]

        if l<2:
            return 0

        return sum(abs(m-i) for i in nums)
