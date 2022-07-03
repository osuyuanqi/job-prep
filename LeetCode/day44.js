console.log(`{I'm back} ${1 + 1}`);

// 237. Delete Node in a Linked List
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function (node) {
  // not del the node, just change val and del the next prop
  node.val = node.next.val;
  node.next = node.next.next;
};
// 122. Best Time to Buy and Sell Stock II
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let profit = 0;
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  return profit;
};

const prices = [7, 1, 5, 3, 6, 4];
console.log(maxProfit(prices));

// 387. First Unique Character in a String
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  const charDic = {};
  for (let i = 0; i < s.length; i++) {
    if (s[i] in charDic) charDic[s[i]][1] += 1;
    else {
      charDic[s[i]] = [i, 1];
    }
  }
  // O(n), check the unique one
  for (const v of Object.values(charDic)) {
    if (v[1] === 1) {
      return v[0];
    }
  }
  return -1;
};

const s = "leetcodel";
console.log(firstUniqChar(s));
// 108. Convert Sorted Array to Binary Search Tree
/**
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */

// Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}
var sortedArrayToBST = function (nums) {
  // terminate condition when loop finished
  if (nums.length === 0) return null;
  let mid = Math.floor(nums.length / 2);
  // only the mid was left
  const root = new TreeNode(nums[mid]);
  // recursive loop, index
  root.left = sortedArrayToBST(nums.slice(0, mid));
  root.right = sortedArrayToBST(nums.slice(mid + 1, nums.length));
  return root;
};
const nums = [-10, -3, 0, 5, 9];
console.log(sortedArrayToBST(nums));

// 268. Missing Number
/**
 * @param {number[]} nums
 * @return {number}
 */
// Hash
var missingNumber = function (nums) {
  const missSet = new Set();
  for (const i of nums) {
    missSet.add(i);
  }
  console.log(missSet);
  for (let j = 0; j < nums.length + 1; j++) {
    if (!missSet.has(j)) {
      return j;
    }
  }
};
// Math method
var missingNumber = function (nums) {
  const sum = nums.reduce((prev, curr) => curr + prev, 0);
  return ((nums.length + 1) * nums.length) / 2 - sum;
};

const nums1 = [4, 3, 2, 1];
console.log(missingNumber(nums1));

// 168. Excel Sheet Column Title
/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function (columnNumber) {
  let res = [];
  while (columnNumber > 0) {
    // use -1
    columnNumber--;
    let remainder = columnNumber % 26;
    // use -1, to avoid the next loop, e.g. 26=>0; if not-1, 26/26===1=>next loop
    columnNumber = Math.floor(columnNumber / 26);

    console.log(res, columnNumber, remainder);
    // tip: not res+=..; to avoid reverse string
    res = String.fromCharCode(remainder + 65) + res;
  }
  return res;
};
const columnNumber = 701;
console.log(convertToTitle(columnNumber));

// 350. Intersection of Two Arrays II
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  const dic = {};
  for (const i of nums1) {
    if (i in dic) {
      dic[i]++;
    } else {
      dic[i] = 1;
    }
  }
  const res = [];
  for (const j of nums2) {
    if (j in dic) {
      dic[j]--;
      if (dic[j] >= 0) res.push(j);
    }
  }
  return res;
};
const nums2 = [4, 9, 5],
  nums3 = [9, 4, 9, 8, 4];
console.log(intersect(nums2, nums3));

// 202. Happy Number
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
  const _set = new Set();
  let nextValue = n;
  while (nextValue != 1) {
    let elem = nextValue.toString().split("");
    let res = 0;
    for (const i of elem) {
      let j = parseInt(i);
      res += j * j;
    }
    // console.log(res)
    nextValue = res;
    // console.log(_set);
    if (!_set.has(nextValue)) {
      _set.add(nextValue);
    } else {
      return false;
    }
  }
  return true;
};
const n = 2;
console.log(isHappy(n));

// 118. Pascal's Triangle
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {};
const numRows = 5;
console.log(generate(numRows));

// 70. Climbing Stairs
/**
 * @param {number} n
 * @return {number}
 */
// way1: intuitive way
var climbStairs = function (n) {
  if (n < 3) {
    return n;
  }
  return climbStairs(n - 1) + climbStairs(n - 2);
};
// way2: default memo, O(n) time complexity, O(n) space complexity
var climbStairs = function (n, memo = { 1: 1, 2: 2 }) {
  if (n in memo) {
    return memo[n];
  }
  memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);
  return memo[n];
};
// way3: swap, O(n) time complexity, O(1) space
var climbStairs = function (n) {
  let prev = 0,
    curr = 1;
  for (let i = 0; i < n; i++) {
    [prev, curr] = [curr, prev + curr];
  }
  return curr;
};
console.log(climbStairs(4));
