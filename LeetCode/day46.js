// 160. Intersection of Two Linked Lists
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
// infinite loop if no intersect
var getIntersectionNode = function (headA, headB) {
  let l1 = headA,
    l2 = headB;
  while (l1 !== l2) {
    // transition to the headB, not l2, since l2 is changing.
    l1 = l1 ? l1.next : headB;
    l2 = l2 ? l2.next : headA;
  }
  return l1;
};

// hash map method
var getIntersectionNode = function (headA, headB) {
  const h1 = new Set();
  while (headA) {
    h1.add(headA);
    headA = headA.next;
  }
  // console.log(h1);
  while (headB) {
    if (h1.has(headB)) {
      return headB;
    }
    headB = headB.next;
  }
  return null;
};
// 172. Factorial Trailing Zeroes
/**
 * @param {number} n
 * @return {number}
 */

// not works in big# pow
var trailingZeroes = function (n) {
  let pow = 1,
    res = 0;
  for (let i = 2; i <= n; i++) {
    pow *= i;
  }
  console.log(pow % 10);
  while (pow % 10 === 0) {
    res++;
    pow = Math.floor(pow / 10);
    console.log(res);
  }
  return res;
};
// way1:
//tip: 1.# of 2>># of 5 => calculate 5 only
// 2. counts the total # of 5, e.g.25= (#5) * 5 + #1 * (#5)=6' 5, which comes 6's 5
var trailingZeroes = function (n) {
  let count = 0;
  while (n != 0) {
    n = Math.floor(n / 5);
    // e.g. 15=(5*3)*14..=
    // 25 = 5*5, #1 of 5 left after first loop
    console.log(n);
    count += n;
  }
  return count;
};
// way2: concers # of 5 only
var trailingZeroes = function (n) {
  let res = 0;
  for (let i = 5; i <= n; i += 5) {
    let j = i;
    while (j % 5 === 0) {
      res++;
      j = Math.floor(j / 5);
    }
  }
  return res;
};
// way3: optimization
var trailingZeroes = function (n) {
  let res = 0;
  for (let i = 5; i <= n; i = i * 5) {
    res += Math.floor(n / i);
  }
  return res;
};
console.log(trailingZeroes(25));

// 20. Valid Parentheses
/**
 * @param {string} s
 * @return {boolean}
 */

var isValid = function (s) {
  const dic = { "}": "{", ")": "(", "]": "[" },
    stack = [];
  for (const i of s) {
    if (i in dic) {
      if (stack.pop() !== dic[i]) return false;
    } else {
      stack.push(i);
    }
  }
  return stack.length === 0;
};
const s = "()";
console.log(isValid(s));

// 141. Linked List Cycle

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
// way1: hash
var hasCycle = function (head) {
  const dic = new Set();
  while (head) {
    if (dic.has(head)) return true;
    dic.add(head);
    head = head.next;
  }
  return false;
};
// way2: two pointers
var hasCycle = function (head) {
  let fast = head,
    slow = head;
  while (fast && fast.next) {
    // if ignore fast only. e.g.[1,2]=>fast.next.next===none, then none.next is not exist
    fast = fast.next.next;
    slow = slow.next;
    if (slow === fast) {
      return true;
    }
  }
  return false;
};

//88. Merge Sorted Array
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  for (let i = 0; i < n; i++) {
    // the (m+i)th value in nums1
    nums1[m + i] = nums2[i];
  }
  nums1.sort((a, b) => a - b);
};
const nums1 = [1, 2, 3, 0, 0, 0],
  m = 3,
  nums2 = [2, 5, 6],
  n = 3;
console.log(merge(nums1, m, nums2, n));
console.log(nums1);

// 155. Min Stack
// this usage is the key1
var MinStack = function () {
  this.stack = [];
  this.minStack = [];
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
  this.stack.push(val);
  // use length to judge is the key2
  if (this.minStack.length !== 0)
    this.minStack.push(Math.min(val, this.minStack[this.minStack.length - 1]));
  else this.minStack.push(val);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  this.stack.pop();
  this.minStack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  return this.minStack[this.minStack.length - 1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
