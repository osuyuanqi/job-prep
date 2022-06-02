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
    if (nums[i] in obj) {
      obj[nums[i]] = 0;
    } else {
      obj[nums[i]] = 1;
    }
  }
  for (const i in obj) {
    if (obj[i] == 1) {
      return i;
    }
  }
};
// bitwise operation
var singleNumber = function (nums) {
  return nums.reduce((acc, pre) => (acc ^= pre), 0);
};

const nums = [4, 1, 2, 2, 1];
console.log(singleNumber(nums));

// 104. Maximum Depth of Binary Tree
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  if (root == null) {
    return 0;
  }
  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
};
// iterative
var maxDepth = function (root) {
  // when the root ==[]
  if (!root) return 0;
  let stack = [root],
    depth = 0;
  while (stack.length) {
    let new_stack = [];
    for (const i of stack) {
      if (i.left) new_stack.push(i.left);
      if (i.right) new_stack.push(i.right);
    }
    // console.log(new_stack)
    // same logic as pop the root elem
    stack = new_stack;
    depth++;
  }
  return depth;
};
console.log(Math.max(2, 3));

//345. Reverse Vowels of a String
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {};
const s1 = "hello";
console.log(reverseVowels(s1));
