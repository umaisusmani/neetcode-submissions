class Solution {
    hasDuplicate(nums: number[]): boolean {
        const seen = new Set<number>();

        for (const num of nums) {
            seen.add(num);
        }

        return seen.size !== nums.length;
    }
}