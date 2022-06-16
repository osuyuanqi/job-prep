// 152. Maximum Product Subarray
/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxProduct = function (nums) {
    let currMax = 1,
      currMin = 1;
    let arr = [],
      res = nums[0];
    for (let i of nums) {
      arr = [i, i * currMax, i * currMin];
      currMax = Math.max(...arr);
      currMin = Math.min(...arr);
      res = Math.max(currMax, res);
      console.log(currMax, currMin);
    }
  
    return res;
  };
  const nums = [2, -5, -2, -4, 3];
  console.log(maxProduct(nums));
  