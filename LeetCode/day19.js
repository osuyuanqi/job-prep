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

// console.log(countAndSay(4));

/*************************************************
 * 242. Valid Anagram
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 ************************************************/

// dictionary method 1
var isAnagram1 = function(s, t) {
    if (s.length!=t.length)return false;
    let dict ={};
    for(let i =0;i<s.length;i++){
        // console.log(dict)
        if (s[i] in dict){
            dict[s[i]]++;
            console.log(dict[s[i]])
        }
        else
            dict[s[i]]=1;
    }
    // console.log(dict);
    for(let j =0;j<t.length;j++){
        // console.log(dict)
        if (t[j] in dict){
            dict[t[j]]--;
        }
        else
            return false;
    }
    for(const k in dict)
    {
        if(dict[k]!=0)return false;
    }
    
    console.log(dict);
    return true;
};
// dic method2: save one operation
var isAnagram = function(s, t) {
    if (t.length !== s.length) return false;
    const counts = {};
    for (let c of s) {
        counts[c] = (counts[c] || 0) + 1;
    }
    for (let c of t) {
        // console.log(counts[c],!counts[c],c,t,counts)
        // do this after got 0 last time. return false since it probe the element again.
        if (!counts[c]) return false;
        counts[c]--;
    }
    return true;
};
let s = "rat", t = "aar";
console.log(isAnagram(s,t));