// 28. Implement strStr()
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
//math tip
var strStr = function (haystack, needle) {
  let maxLen = haystack.length - needle.length + 1;
  if (maxLen > 0) {
    for (let i = 0; i < maxLen; i++) {
      if (haystack.slice(i, i + needle.length) === needle) {
        //   console.log(i);
        return i;
      }
    }
  }
  return -1;
};
const haystack = "hello",
  needle = "ll";
console.log(strStr(haystack, needle));

// 69. Sqrt(x)
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  let res = 1;
  while (res * res < x) {
    res++;
  }
  return res * res === x ? res : res - 1;
};

// binary cut
var mySqrt = function (x) {
  let low = 0,
    high = x,
    p = 0;
  // console.log(low, high);
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    let m = mid * mid;
    if (m > x) {
      high = mid - 1;
    } else if (m < x) {
      // store the lowest val
      p = mid;
      low = mid + 1;
    } else {
      return mid;
    }
  }
  return p;
};

console.log(mySqrt(9));

// 190. Reverse Bits
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  // padStart(32,'0'), start with 0, the total is 32 bits.
  let str = parseInt(n)
    .toString(2)
    .padStart(32, "0")
    .split("")
    .reverse()
    .join("");
  return parseInt(str, 2);
  console.log(parseInt(str, 2));
};
const n = "00000010100101000001111010011100";
console.log(reverseBits(n));
// 704. Binary Search
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let low = 0,
    high = nums.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (nums[mid] < target) {
      low = mid + 1;
    } else if (nums[mid] > target) {
      high = mid - 1;
    } else return mid;
  }
  return -1;
};
const nums = [-1, 0, 3, 5, 9, 12],
  target = 9;
console.log(search(nums, target));
