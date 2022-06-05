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

// console.log(fizzBuzz(3));

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

// const nums = [4, 1, 2, 2, 1];
// console.log(singleNumber(nums));

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
// 206. Reverse Linked List
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let prev = null,
    curr = head;
  while (curr != null) {
    let temp = curr.next;
    curr.next = prev;
    prev = curr;
    curr = temp;
  }
  return prev;
};
//recursive way
var reverseList = function (head) {
  // stpe1: recursive reverse, since head should be the last elem after reverse
  if (head === null || head.next === null) {
    return head;
  }
  const rev = reverseList(head.next);
  // console.log(head,rev)
  // step2: point the second elem to the first elem, second->first&&first->second this time.
  head.next.next = head;
  // step3: unlock the first-> second to first->null, so that it only points to one dircetion
  head.next = null;
  return rev;
};

// 371. Sum of Two Integers
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function (a, b) {
  while (b != 0) {
    let carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }
  return a;
};

// 171. Excel Sheet Column Number
/**
 * @param {string} columnTitle
 * @return {number}
 */
// double convert
var titleToNumber = function (columnTitle) {
  const dic = {};
  let res = 0;
  for (let i = 0; i < 26; i++) {
    dic[String.fromCharCode(i + 65)] = i + 1;
  }
  console.log(dic);
  // res=columnTitle.reduce((prev,curr) => {curr

  // },0);
  let lenCol = columnTitle.length;
  for (let i = 0; i < columnTitle.length; i++) {
    console.log(dic[columnTitle[i]]);
    res += dic[columnTitle[i]] * 26 ** (lenCol - 1);
    lenCol--;
  }
  return res;
};
// convert once
var titleToNumber = function (columnTitle) {
  let lenCol = columnTitle.length,
    res = 0;
  for (let i = 0; i < columnTitle.length; i++) {
    //   console.log(columnTitle[i].charCodeAt(0)-64);
    const val = columnTitle[i].charCodeAt(0) - 64;
    res += val * 26 ** (lenCol - 1);
    lenCol--;
  }
  return res;
};

// console.log(titleToNumber("ZY"));

// 283. Move Zeroes
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var moveZeroes = function (nums) {
  let left = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != 0) {
      [nums[i], nums[left]] = [nums[left], nums[i]];
      //just skip the 0,
      left++;
      console.log(nums);
    }
  }
};
// backwards method,
var moveZeroes = function (nums) {
  for (let i = nums.length - 1; i >= 0; i--) {
    //1,0,0->pop the last 0 and push another 0
    if (nums[i] === 0) {
      nums.splice(i, 1);
      nums.push(0);
    }
  }
  return nums;
};
// !important: not work sinc it will skip the exchanged one. e.g.[1,0,0]->[0,1,0]=>the first 0 won't be exchange.
var moveZeroes1 = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    //1,0,0->pop the last 0 and push another 0
    if (nums[i] === 0) {
      nums.splice(i, 1);
      nums.push(0);
    }
  }
  return nums;
};

// const nums1 = [0, 0, 1];
// console.log(moveZeroes(nums1), nums1);

//345. Reverse Vowels of a String
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  let sA = s.toLowerCase().split("");
  console.log(sA);
  let l = 0,
    r = sA.length - 1;
  while (l < r) {
    console.log(l, r);
    // 1.get the vowel elem,l keeps adding less than r, or it will reverse again
    while (
      s[l] != "a" &&
      s[l] != "e" &&
      s[l] != "i" &&
      s[l] != "o" &&
      s[l] != "u" &&
      l < r
    ) {
      l++;
    }

    while (
      s[r] != "a" &&
      s[r] != "e" &&
      s[r] != "i" &&
      s[r] != "o" &&
      s[r] != "u" &&
      l < r
    ) {
      r--;
    }
    // 2.swap
    [sA[l], sA[r]] = [sA[r], sA[l]];
    // 3.move shrinkly
    l++;
    r--;
  }
  return sA.join("");
};
// const s1 = "hello";
// console.log(reverseVowels(s1));
