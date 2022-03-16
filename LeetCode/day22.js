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
console.log(missingNumber(nums));

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
