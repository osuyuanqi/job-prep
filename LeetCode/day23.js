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
 * 21. Merge Two Sorted Lists
 ***********************************************/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    if (!l1||!l2)return l1||l2;
    let node = new ListNode(-1);
    let cur = node;
    while (l1&&l2){
        if (l1.val<l2.val){
            node.next = l1;
            l1=l1.next;
        }else{
            node.next= l2;
            l2=l2.next;
        }
        node = node.next;
    }
    if(l1) node.next =l1;
    if(l2) node.next=l2;
    return cur.next;
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

/*************************************************
 * 121. Best Time to Buy and Sell Stock
 ***********************************************/

/**
 * @param {number[]} prices
 * @return {number}
 */
// max profits-min profits
var maxProfit = function(prices) {
    let minV=prices[0],maxV=0,profits=0;
    for(let i =1;i<prices.length;i++){
        if(prices[i]<minV)
            minV=prices[i];
        if(prices[i]-minV>profits)
            profits=prices[i]-minV
    }
    return profits;
}
var prices=[7,1,5,3,6,4]
// console.log(maxProfit(prices));
/*************************************************
 * 122. Best Time to Buy and Sell Stock II
 ***********************************************/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let i =0,profit=0,buy=0,sell=0,N=prices.length-1;
    while(i<N){
        if(i<N&&prices[i]>=prices[i+1])
            i++;
        buy = prices[i];

        if(i<N&&prices[i+1]>prices[i])
            i++;
        sell=prices[i];
        profit+=sell-buy;
    }

    return profit;
};
// O(n),add every profits together
var maxProfit = function(prices) {
    let profits=0;
    for(let i=0;i<prices.length-1;i++){
        let a = prices[i+1]-prices[i]
        if(prices[i+1]>prices[i])
            profits+=a;
    }
    return profits;
}
// var prices = [7,1,5,3,6,4]
// console.log(maxProfit(prices));


/*************************************************
 * 387. First Unique Character in a String
 ***********************************************/

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
     var map=new Map();
    for(i=0;i<s.length;i++){
         if(map.has(s[i])){
             map.set(s[i],2);
         }
         else{
             map.set(s[i],1);
         }
     }

    for(i=0;i<s.length;i++){
        if(map.has(s[i]) && map.get(s[i])===1){
            return i;
        }
    }
    return -1;
};

var s="loveleetcode";
console.log(firstUniqChar(s))