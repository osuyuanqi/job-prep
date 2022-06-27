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
