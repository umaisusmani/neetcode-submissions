class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        for (let i=0;i< nums.length;i++)
        {
            let j=nums.indexOf(target - nums[i], i + 1);
            if (j !== -1)
            {
                return [i,j];
            }
        }
        return [0,0];
    }
}
