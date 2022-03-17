/*************************************************
 * tips: set/dic
 ************************************************/
// dic/set added
let dic = {0:1}
let set = new Set()
for(let i =0;i<3;i++)
{   dic[i]+=1;
    set.add(dic[i])
}
// console.log(dic,set);
// Set->Array
nums = [9,4,9,8,4]
set=new Set(nums)
// console.log(set,Array.from(set));

/*************************************************
 * tips: array usage
 ************************************************/

// array in->index
let arr=[2,3,4]
for(let j in arr)
console.log(j);
// array of->value
for(let j of arr)
console.log(j);

// NaN: this value is "number" type 
let a=1+NaN;
console.log(typeof 1+NaN)//numberNaN
console.log(typeof NaN)//number
console.log(a)//NaN