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
