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
// binary cut
var mySqrt = function (x) {
  let low = 0,
    high = x,
    p = 0;
  console.log(low, high);
  while (low <= high) {
    const mid = Math.floor(low + high);
    if (mid * mid > x) {
      high--;
    } else if (mid * mid < x) {
      // store the lowest val
      p = mid;
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return p;
};
console.log(mySqrt(16));
