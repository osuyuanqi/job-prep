/**190. Reverse Bits
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  // console.log()
  let b = n.toString(2);
  // console.log(b)
  let a = b.padStart(32, "0");
  // console.log(a);supplement 0
  let rev = a.split("").reverse().join("");
  return parseInt(rev, 2);
};

// 125. Valid Palindrome
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const a = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  return a.split("").reverse().join("") === a;
};
let s = "A man, a plan, a canal: Panama";
console.log(isPalindrome(s));
