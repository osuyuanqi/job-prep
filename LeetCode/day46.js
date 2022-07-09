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
 var getIntersectionNode = function(headA, headB) {
    let l1=headA,l2=headB;
    while (l1!==l2){
        // transition to the headB, not l2, since l2 is changing.
        l1=l1?l1.next:headB;
        l2=l2?l2.next:headA;
    }
    return l1;
};

// 
var getIntersectionNode = function(headA, headB) {
    const h1=new Set()
    for (let i of headA){
        h1.add(i)
        i=i.next;
    }
}