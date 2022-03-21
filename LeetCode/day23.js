/*************************************************
 * 206. Reverse Linked List
 ***********************************************/

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
// iterative
var reverseList = function(head) {
    if (head == undefined || head.next==undefined){return head;}
    let prev = null;
    let curr = head;
    // console.log(curr);
    
    while (curr){
        let next = curr.next;
        curr.next = prev
        prev = curr;
        curr = next;
    }
    // console.log(prev);
    return prev
};

//recursive
var reverseList = function(head) {
    if (head == undefined || head.next==undefined){return head;}
    let rev = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    // console.log(prev);
    return rev
};


/*************************************************
 * 108. Convert Sorted Array to Binary Search Tree
 ***********************************************/


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    // also works: nums==null||nums.length==0
    if (nums==null ||!nums.length) return null;
    // let->changed before next function,const->changed each time     
    let mid = Math.floor(nums.length/2);
    const root = new TreeNode(nums[mid]);
    root.left = sortedArrayToBST(nums.slice(0,mid))
    // mid+1->since root occupies one element
    root.right = sortedArrayToBST(nums.slice(mid+1,nums.length))
    return root;
    
};


/*************************************************
 * 23. Merge k Sorted Lists
 ***********************************************/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

var mergeKLists = function(lists) {
    const mergeTwo = (l1,l2)=>{
        let node = new ListNode(0)
        let curr=node;
        while (l1&&l2){
            if(l1.val<l2.val){
                node.next=l1;
                l1=l1.next;
            }
            else{
                node.next=l2;
                l2=l2.next;
            }
            node =node.next;
        }
        if (l1){node.next = l1;}
        if (l2){node.next = l2;}
        return curr.next;
    }
    // nk*lgn,root changes in the function
    let root = lists[0];
    for(let i =1;i<lists.length;i++){
        root = mergeTwo(root,lists[i]);
    }
    return root||null;
};