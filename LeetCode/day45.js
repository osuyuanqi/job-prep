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
var hammingWeight = function (n) {
  n = n.toString(2);
  let count = 0;
  for (let i of n) {
    if (i === "1") count++;
  }
  return count;
};
var hammingWeight = function (n) {
  let res = 0;
  while (n != 0) {
    // count #of 1===sum 1
    // last digit: 1011&1=>1,0,1,1
    res += n & 1;
    n >>>= 1;
    console.log(n);
  }
  return res;
};
console.log(hammingWeight(11));

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

// two pointers: return # of unique, no matter what duplicates left behind
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

// 66. Plus One
/**
 * @param {number[]} digits
 * @return {number[]}
 */
// big int method
var plusOne = function (digits) {
  const total = digits.reduce((prev, curr) => (prev += curr.toString()), "");
  // console.log(digits)
  const intV = BigInt(total) + BigInt(1);
  return intV
    .toString()
    .split("")
    .map((a) => BigInt(a));
};
// test cases: 1.big #; 2.===9=>unshift; 3. <9=>+1 directly
var plusOne = function (digits) {
  let lenDig = digits.length - 1;
  while (true) {
    // lastElem++;
    if (digits[lenDig] !== 9) {
      digits[lenDig]++;
      return digits;
    } else {
      digits[lenDig] = 0;
      lenDig--;
      if (lenDig < 0) {
        digits.unshift(1);
        return digits;
      }
    }
  }
};
// const digits = [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3];
const digits = [8, 9, 9];
console.log(plusOne(digits));
