Special Triplets Solution
Problem Statement
Find the count of special triplets in an array where a triplet (i, j, k) is considered special if:

i < j < k (indices are in strictly increasing order)
nums[i] + nums[k] = 2 * nums[j] (the middle element is the arithmetic mean of the first and third)

Solution Approach
This solution uses a three-pointer sliding window technique with hash maps to efficiently count valid triplets.
Algorithm Overview
The key insight is to iterate through each element as the middle element nums[j], while maintaining:

Left Counter: Elements that have appeared before position j
Right Counter: Elements that will appear after position j

For each middle element x, we look for pairs where:

Left element = 2*x
Right element = 2*x

This ensures: 2*x + 2*x = 2 * (2*x) which simplifies to the arithmetic mean property.
Step-by-Step Process

Initialize: Count all elements in the right counter
Iterate: For each element at position j:

Remove it from right (it's no longer "to the right")
Check if 2*x exists in both left and right
Count valid triplets: left[2*x] * right[2*x]
Add current element to left counter


Return: Total count modulo 10^9 + 7
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
