/************************************************
 * 217. Contains Duplicate
 * @param {number[]} nums
 * @return {boolean}
 ***********************************************/

var containsDuplicate1 = function(nums) {
    let set =new Set();
    for(let i of nums){
    	// console.log(nums[i])
    	if (!set.has(i)){
    		set.add(i);
    	}
    	else return true;
    }
    return false;
};

var containsDuplicate = function(nums) {
    let set =new Set(nums);
    console.log(set.size,nums.length)
    return set.size==nums.length;
};

let nums=[1,2,3,4]

console.log(containsDuplicate(nums))



/*************************************************
 * tips: for..in->attibute,for..of->value
 ************************************************/

// let nums=[1,2,3,1]
// for(let i in nums){
// 	console.log(i);
// }
// for(let i of nums){
// console.log(i)
// }