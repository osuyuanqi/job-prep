// 680. Valid Palindrome II
/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function (s) {
  //   if (s.length < 2) return false;
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
const s = "abdeaedca";
console.log(validPalindrome(s));
