
Complexity Analysis

Time Complexity: O(n)

Single pass through the array
Hash map operations are O(1) average case


Space Complexity: O(n)

Two hash maps storing at most n unique elements



Examples
Example 1
pythonnums = [1, 2, 3, 4]
Valid triplet: (1, 2, 3) where 1 + 3 = 2 * 2
Output: 1
Example 2
pythonnums = [2, 4, 6, 4, 2]
Valid triplets: 
- (2, 4, 6): indices (0, 1, 2)
- (2, 4, 6): indices (0, 3, 2)
- (2, 4, 6): indices (4, 1, 2)
- (2, 4, 6): indices (4, 3, 2)
Output: 4
Usage
pythonsolution = Solution()
result = solution.specialTriplets([1, 2, 3, 4])
print(result)  # Output: 1
Key Insights

Arithmetic Mean Property: The condition nums[i] + nums[k] = 2 * nums[j] means nums[j] is the arithmetic mean of nums[i] and nums[k]
Efficient Counting: By fixing the middle element and using counters, we avoid nested loops (which would be O(n³))
Modulo Operation: Results are returned modulo 10^9 + 7 to handle large counts

Edge Cases

Empty array: Returns 0
Array with fewer than 3 elements: Returns 0
All elements are the same: Counts all possible triplet combinations
No valid triplets exist: Returns 0

License
This solution is provided as-is for educational purposes.
