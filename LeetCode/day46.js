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
//5*2=10 is the unique key

var trailingZeroes = function (n) {
  let count = 0;
  while (n > 0) {
    n = Math.floor(n / 5);
    count += n;
  }
  return count;
};











// tip: counts the # of 5, e.g.30=5*6, which comes 6's 5
var trailingZeroes = function (n) {
let count=0;
while (n!=0){
    n=Math.floor(n/5);
    // e.g. 15=(5*3)*14..=
    console.log(n)
    count+=n;
}
return count;
}
console.log(trailingZeroes(15));
