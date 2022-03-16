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

// console.log(generate(4));
/*************************************************
 * 70. Climbing Stairs
 * @param {number} n
 * @return {number}
 ************************************************/

// iterative->swap
var climbStairs = function(n) {
    if (n < 4) return n;
    let second=2,third=3;
    for(let i =4;i<n+1;i++){
        let temp=0;
        temp=second;
        second=third;
        third =second+temp; 
    }
    return third;
    // return climbStairs(n-1)+climbStairs(n-2);
};
// iterative->hash array
var climbStairs = function(n) {
    let res = [];
    res[0]=1,res[1]=2;
    for(let i =2;i<=n;i++)
        res[i]=res[i-1]+res[i-2];
    return res[n];
}
// recursive->hash dic/array
// let memo={1:1,2:2,3:3}
let memo=[0,1,2,3]
var climbStairs = function(n) {
    if (memo[n]!=undefined) return memo[n];
    // res = 
    memo[n]=climbStairs(n-1)+climbStairs(n-2);
    return memo[n]
};

// console.log(climbStairs(45))


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