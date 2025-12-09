class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        right = Counter(nums)
        left = Counter()

        ans = 0

        for x in nums:
            right[x] -= 1           # remove count from right map

            target = 2 * x

            if target in left and target in right:
                ans = (ans + left[target] * right[target]) % MOD

            left[x] += 1            # move x into the left map

        return ans
