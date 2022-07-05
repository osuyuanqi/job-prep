// 53. Maximum Subarray
/**
 * @param {number[]} nums
 * @return {number}
 */
// dynamic programming 1: max(prev, curr), O(n)
var maxSubArray = function (nums) {
  const res = Array(nums.length).fill(0);
  res[0] = nums[0];
  for (let i = 1; i < nums.length; i++) {
    res[i] = nums[i] + res[i - 1];
    if (res[i] < nums[i]) res[i] = nums[i];
    // console.log(`${nums[i]},${res[i - 1]}`);
  }
  return Math.max(...res);
};
// dynamic programming 2: prev<0 =>x, O(n)
var maxSubArray = function (nums) {
  const maxV = nums[0];
  for (let i = 1; i < nums.length; i++) {
    // concern the positive prev only
    if (nums[i - 1] > 0) {
      nums[i] += nums[i - 1];
    }
  }
  return Math.max(...nums);
};
const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
console.log(maxSubArray(nums));

// 326. Power of Three
/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {
  if (n === 0) return false;
  if (n === 1) return true;
  while (n !== 0) {
    if (n % 3 === 0) {
      n = Math.floor(n / 3);
      if (n !== 1) continue;
      else return true;
    }
    return false;
  }
  return true;
};
// much shorter logic
var isPowerOfThree = function (n) {
  if (n > 0) {
    while (n % 3 === 0) n = Math.floor(n / 3);
  }
  return n === 1;
};
console.log(isPowerOfThree(9));

// 191. Number of 1 Bits
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {};
console.log(hammingWeight(1));

// 1. Two Sum
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
    }
    dic[nums[i]] = i;
  }
};
const nums1 = [2, 7, 11, 15],
  target = 9;
console.log(twoSum(nums1, target));

// 26. Remove Duplicates from Sorted Array
/**
 * @param {number[]} nums
 * @return {number}
 */

// return # of unique, no matter what duplicates left behind
var removeDuplicates = function (nums) {
  let l = 1;
  for (let r = 1; r < nums.length; r++) {
    if (nums[r] != nums[r - 1]) {
      nums[l] = nums[r];
      l++;
    }
  }
  return l;
};
const nums2 = [1, 1, 2];
console.log(removeDuplicates(nums2));
