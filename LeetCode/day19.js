/**
 * 53. Maximum Subarray
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let max = -Infinity;
    let temp = 0;
    for (let i =0; i<nums.length;i++){
        console.log("i=",i,"\tnums=",nums[i],"\ttemp,num+temp=",temp,nums[i]+temp,"\tmax=",Math.max(nums[i],nums[i]+temp))
        // from the temp max to explore until find the maximum one
        temp = Math.max(nums[i],nums[i]+temp)
            console.log(temp)

        if (temp > max){
            console.log("maxt",temp)
            max = temp;
        }
    }
    return max;
};

const nums = [-2,1,-3,4,-1,2,1,-5,4];
console.log(maxSubArray(nums));