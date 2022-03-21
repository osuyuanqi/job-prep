/*************************************************
 * tips: set/dic
 ************************************************/
// dic/set added
let dic = {0:1}
let set = new Set()
let map = new Map();
for(let i =0;i<3;i++)
{   dic[i]+=1;
    set.add(dic[i]);
    // map[dic[i]]=i;just set property,can't access
    map.set(i,"[map]"+i)
}
console.log(dic,"==",set,"==",map);
console.log(0 in dic)
console.log(set.has(2))
console.log(map.has(2))

for(let i =0;i<map.size;i++)
console.log(map.get(i),"===")

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