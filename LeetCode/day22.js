/*************************************************
 * 268. Missing Number
 ***********************************************/

/**
 * @param {number[]} nums
 * @return {number}
 */
// minus method
var missingNumber = function(nums) {
    let s=0;
    for(let i=1;i<=nums.length;i++){
        s+=i;
    }
    return s-nums.reduce((a,b)=>{return a+b;},0)
};
// improved minus method
var missingNumber = function(nums) {
    let res=nums.length,s=0;
    for(let i =0;i<nums.length;i++){
        res += i;
        s+=nums[i];
    }
    return (res - s)
}
// hash map
var missingNumber = function(nums) {
    let set =new Set();
    for(let i =0;i<nums.length;i++){
        set.add(nums[i]);
    }
    // console.log(set)
    for(let i =0;i<=nums.length;i++){
        if (!set.has(i))
            return i
    }
}
let nums = [3,0,1,2]
// console.log(missingNumber(nums));

/*************************************************
 * 237. Delete Node in a Linked List
 ***********************************************/

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
var deleteNode = function(node) {
    node.val=node.next.val;
    node.next = node.next.next;
};

/*************************************************
 350. Intersection of Two Arrays II
 ***********************************************/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
     let arr = [],dict={}
     for(let i of nums1){
        dict[i]= dict[i]?dict[i]++:1
     }
     console.log(dict)
     for(let j of nums2){
        if (dict[j]){
            dict[j]--;
            arr.push(j)
        }
     }
     return arr;
    }
let  nums1 =  [4,9,5], nums2 = [9,4,9,8,4]
console.log(intersect(nums1,nums2));
/*************************************************
 * 155. Min Stack
 ***********************************************/

var MinStack = function() {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
