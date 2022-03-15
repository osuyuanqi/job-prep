/************************************************
 * 217. Contains Duplicate
 * @param {number[]} nums
 * @return {boolean}
 ***********************************************/

// way1:hash
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
// way2: length compare
var containsDuplicate = function(nums) {
    let set =new Set(nums);
    // console.log(set.size,nums.length)
    return set.size!=nums.length;
};

let nums=[1,2,3,4]

// console.log(containsDuplicate(nums))

/************************************************
 * 118. Pascal's Triangle
 * @param {number} numRows
 * @return {number[][]}
 ***********************************************/

var generate = function(numRows) {
    let res =[];
    for(let i= 0;i<numRows;i++){
        res[i]=[];
        res[i][0]=res[i][i]=1;
        for(let j=1;j<i;j++)
        {
            res[i][j]=res[i-1][j-1]+res[i-1][j];
        }
    }
    return res;
};

console.log(generate(4));

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