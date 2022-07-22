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

console.log(mySqrt(214739560));
