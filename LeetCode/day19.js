/************************************************
 * 53. Maximum Subarray
 * @param {number[]} nums
 * @return {number}
 ***********************************************/
var maxSubArray = function(nums) {
    let max = -Infinity;
    let temp = 0;
    for (let i =0; i<nums.length;i++){
        console.log("i=",i,"\tnums=",nums[i],"\ttemp,num+temp=",temp,nums[i]+temp,"\tmax=",Math.max(nums[i],nums[i]+temp))
        // from the temp max to explore until find the maximum one
        temp = Math.max(nums[i],nums[i]+temp)
            console.log(temp);

        if (temp > max){
            console.log("maxt",temp)
            max = temp;
        }
    }
    return max;
};

// const nums = [-2,1,-3,4,-1,2,1,-5,4];
// console.log(maxSubArray(nums));

/************************************************
 * 38. Count and Say
 * @param {number} n
 * @return {string}
 ***********************************************/

// iterative
var countAndSay = function(n) {
    let res = "1";
    while (n>1){
    let presentValue=res[0],temp="",count=0;
    for(let i=0;i<res.length;i++){
        // calculate the #
        if(res[i]==presentValue){
            count++;
        }
        // move to the different value
        else{
            // store the present state first
            temp+=count+presentValue;
            // begin the second calculation
            count=1;
            presentValue=res[i];
        }
    }
    // console.log(res,"temp=",temp,"aaa",count,presentValue)
    // end with first temp string + the final state(count+presentValue)
    res = temp+count+presentValue;
    n--;
    }
    return res;
}
// recursive
var countAndSay1 = function(n,res = "1") {
    if(n===1) return res;
    let presentValue=res[0],temp="",count=0;
    for(let i=0;i<res.length;i++){
        if(res[i]==presentValue){
            count++;
        }
        else{
            temp+=count+presentValue;
            count=1;
            presentValue=res[i];
        }
    }
        // console.log(res,count,presentValue)
    return countAndSay(n-1,temp+count+presentValue);
}

console.log(countAndSay(4));