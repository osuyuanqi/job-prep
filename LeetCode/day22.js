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
 note the test cases
 ***********************************************/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 // dict "of" usage, O(n)
var intersect = function(nums1, nums2) {
     let arr = [],dict={}
     for(let i of nums1){
        dict[i]= dict[i]?dict[i]+1:1
     }
     // console.log(dict)
     for(let j of nums2){
        if (dict[j]){
            dict[j]--;
            arr.push(j)
        }
     }
     return arr;
    }

// rank->push orderly,O(n)
var intersect = function (nums1,nums2) {
    // default sort: convert to string and ascend by Unicode value.
    nums1.sort((a,b)=>{return a-b});
    nums2.sort((a,b)=>{return a-b});
    // nums2.sort();
    // console.log(nums2)
    // nums2.sort((a,b)=>{return a-b});
    // console.log(nums2)

    let i=0,j=0,arr=[];
    while (i<nums1.length && j<nums2.length){
        if (nums1[i]==nums2[j]){
            arr.push(nums1[i]);
            i++;
            j++;
        }
        else if(nums1[i]<nums2[j]) i++;
        else j++;
    }
    return arr;
}
// let  nums1 =  [4,9,5], nums2 = [9,4,9,8,4]
// let nums1 = [1,2,2,1], nums2 = [2,2]
// let nums1=[61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
// nums2=[5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]
// console.log(intersect(nums1,nums2));



/*************************************************
 * 349. Intersection of Two Arrays
 ***********************************************/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let set = new Set(nums1);
    // let res = new Set();
    // for(let j of nums2)
    //     if(set.has(j)){
    //         res.add(j);
    //     }
    let res = new Set(nums2.filter(x=>set.has(x)));
    return Array.from(res);
};

let  nums1 =  [4,9,5], nums2 = [9,4,9,8,4]
// let nums1 = [1,2,2,1], nums2 = [2,2]
// console.log(intersection(nums1,nums2));

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
