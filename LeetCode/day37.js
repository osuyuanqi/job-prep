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
// console.log(isPalindrome(s));

// 189. Rotate Array
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (numsa, k) {
  const newK = k % nums.length;
  let newA = nums.splice(-newK);
  nums.splice(0, 0, ...newA);
};
(nums = [1, 2, 3, 4, 5, 6, 7]), (k = 3);
// rotate(nums, k);
// console.log(nums);

// 7. Reverse Integer
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const sign = x > 0 ? 1 : -1;
  let a = x * sign;
  let b = a.toString().split("").reverse().join("");
  let res = sign * parseInt(b);
  return res > (-2) ** 31 && res < 2 ** 31 - 1 ? res : 0;
};

var reverse = function (x) {
  const sign = x > 0 ? 1 : -1;
  let a = x * sign;
  ([res,c])=([0,0])
  while (a) {
     res = a % 10+res*10;
    a=Math.floor(a/10);
    console.log(res,a);
  }
  res *= sign;
  return res > (-2) ** 31 && res < 2 ** 31 - 1 ? res : 0;
};

const x = -123;
// console.log(reverse(x));

// 344. Reverse String
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
// built-in function
var reverseString = function(s) {
  s.reverse().join("");
};
// swap
var reverseString = function(s) {
  let l=0,r=s.length-1;
  while (l<r){
    [s[l],s[r]]=[s[r],s[l]]
    l++;
    r--;
  }
};
s = ["h","e","l","l","o",'a'];
// reverseString(s);
// console.log(s);

