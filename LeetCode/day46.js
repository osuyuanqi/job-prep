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
console.log(trailingZeroes(25));
