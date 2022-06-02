// 344. Reverse String
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 * input is array, so in-place works
 */
var reverseString = function (s) {
  let l = 0,
    r = s.length - 1;
  while (l < r) {
    let temp = s[l];
    s[l] = s[r];
    s[r] = temp;
    l++;
    r--;
  }
};
let s = ["h", "e", "l", "l", "o"];
reverseString(s);
console.log(s);

// 412. Fizz Buzz
/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function (n) {
  let res = [];
  for (let i = 1; i < n + 1; i++) {
    if (i % 15 === 0) {
      res.push("FizzBuzz");
    } else if (i % 3 === 0) {
      res.push("Fizz");
    } else if (i % 5 === 0) {
      res.push("Buzz");
    } else {
      res.push(i.toString());
    }
  }
  return res;
};

console.log(fizzBuzz(3));

// 136. Single Number
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  const obj = {};
  for (let i = 0; i < nums.length; i++) {
      if (nums[i] in obj){
        obj[nums[i]]=0;
      }
      else{
        obj[nums[i]]=1
      }
  }
  for(const i in obj){
      if (obj[i]==1){
          return i
      }
  }
};
// bitwise operation
var singleNumber = function(nums) {
    return nums.reduce((acc,pre)=>acc^=pre,0)
 };

const nums = [4,1,2, 2, 1];
console.log(singleNumber(nums));



















//345. Reverse Vowels of a String
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {};
const s1 = "hello";
console.log(reverseVowels(s1));
