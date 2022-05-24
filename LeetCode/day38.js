// 680. Valid Palindrome II
/**
 * @param {string} s
 * @return {boolean}
 */
// way1: consider odd and left
var validPalindrome = function (s) {
  let l = 0,
    r = s.length - 1;
  let arr = [];
  // res = 0;
  while (l < r) {
    if (s[l] !== s[r]) {
      // even:abccda,compare bccd
      let even = s.substring(l, r);
      // odd: move right totally, pass one and compare right. e.g.abdeaedca->deaedc or bdeaed
      // exclude end
      let odd = s.substring(l + 1, r + 1);
      return (
        even === even.split("").reverse().join("") ||
        odd === odd.split("").reverse().join("")
      );
    }
    l++;
    r--;
  }
  return true;
};
// way2: move left and right explaination
function isPar(s) {
    // console.log(s)
    return s===s.split("").reverse().join("")
}
var validPalindrome = function (s) {
  let l = 0,
    r = s.length - 1;
  let arr = [];
  // res = 0;
  while (l < r) {
    if (s[l] !== s[r]) {
        // move right, skip l->[l+1,r+1) ;or move left, skip r->[l,r)
        // console.log(s[l],s[r])
      return isPar(s.substring(l+1,r+1))||isPar(s.substring(l,r));
    }
    l++;
    r--;
  }
  return true;
};
const s = "aeab";
console.log(validPalindrome(s));
