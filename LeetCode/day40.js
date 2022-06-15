// 1. two sum
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const dic = {};
  for (let i = 0; i < nums.length; i++) {
    if (target - nums[i] in dic) {
      return [dic[target - nums[i]], i];
    } else {
      dic[nums[i]] = i;
      console.log(dic);
    }
  }
};

const nums = [2, 7, 11, 15],
  target = 9;
console.log(twoSum(nums, target));

// 121. Best Time to Buy and Sell Stock
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minv = prices[0],
    profits = 0;
  for (let i of prices) {
    if (i < minv) {
      minv = i;
    }
    if (i - minv > profits) {
      profits = i - minv;
    }
  }
  return profits;
};
const prices = [7, 1, 5, 3, 6, 4];
console.log(maxProfit(prices));
// 217. Contains Duplicate
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let st = new Set(nums);
  return st.size !== nums.length;
};

var containsDuplicate = function (nums) {
  let st = {};
  for (const i of nums) {
    if (i in st) return true;
    else {
      st[i] = 0;
    }
  }
  return false;
};

var containsDuplicate = function (nums) {
  let st = new Set();
  for (const i of nums) {
    if (st.has(i)) return true;
    else {
      st.add(i);
    }
  }
  return false;
};

console.log(containsDuplicate([1, 2, 3, 4, 1]));
// 219. Contains Duplicate II
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
// sliding window: just manipulate 1 elem each time
var containsNearbyDuplicate = function (nums, k) {
  const dic = {};
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in dic && i - dic[nums[i]] <= k) {
      return true;
    } else {
      dic[nums[i]] = i;
    }
  }
  console.log(dic, count, k);
  return false;
};
const nums1 = [1, 2, 3, 1],
  k = 3;
console.log(containsNearbyDuplicate(nums1, k));
// 238. Product of Array Except Self
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let arr = [];
  for (let i = 0; i < nums.length; i++) {
    let res = 1;
    for (let j = 0; j < nums.length; j++) {
      if (i === j) {
        continue;
      } else {
        res *= nums[j];
      }
    }
    arr.push(res);
  }
  console.log(arr);

  return arr;
};

var productExceptSelf = function (nums) {
  //leftmost: except itself,from nums[0]=1,since there isn't any elem from the left
  let prefix = 1;
  const leftmost = [];
  for (let i = 0; i < nums.length; i++) {
    leftmost[i] = prefix;
    prefix = prefix * nums[i];
  }
  console.log(leftmost);
  //rightmost: except itself first loop val= 1 since no elem from rigghtmost
  let sufix = 1;
  const rightmost = [];
  for (let j = nums.length - 1; j >= 0; j--) {
    rightmost[j] = sufix;
    sufix *= nums[j];
  }
  console.log(rightmost);
  //combine the leftmost and rightmost, except itself
  const res = [];
  for (let k = 0; k < nums.length; k++) {
    res[k] = leftmost[k] * rightmost[k];
  }
  return res;
};

const nums2 = [1, 2, 3, 4];
console.log(productExceptSelf(nums2));
// 53. Maximum Subarray
/**
 * @param {number[]} nums
 * @return {number}
 */
//sliding window: move 1 elem each time, compare prev ele(res) and curr
var maxSubArray = function (nums) {
  let sum = 0,
    res = -Infinity;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    // res store the prev max result
    res = Math.max(res, sum);
    sum = sum > 0 ? sum : 0;
    console.log(sum, res);
  }
  return res;
};
//dp method
var maxSubArray = function (nums) {
  const dp = new Array(nums.length).fill(0);
  dp[0] = nums[0];
  for (let i = 1; i < nums.length; i++) {
    //only leave the max dp[n-1], then to the current dp[i]
    dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
  }
  console.log(dp);
  return dp.reduce((prev, curr) => Math.max(prev, curr), -Infinity);
};

// only care the >0 elem previously, since it would decrease the total value
var maxSubArray = function (nums) {
  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] > 0) {
      nums[i] += nums[i - 1];
    }
  }
  return nums.reduce((prev, curr) => Math.max(prev, curr), -Infinity);
};

const nums3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
// const nums3 = [-2, -1, -3];
console.log(maxSubArray(nums3));
