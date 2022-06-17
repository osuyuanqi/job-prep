// 152. Maximum Product Subarray
/**
 * @param {number[]} nums
 * @return {number}
 */
// dp: need to store negative, since it might larger when counters another negative value
// only need max value, so no need to extra space to store same max value
var maxProduct = function (nums) {
  let currMax = 1,
    currMin = 1;
  let arr = [],
    res = nums[0];
  for (let i of nums) {
    arr = [i, i * currMax, i * currMin];
    currMax = Math.max(...arr);
    currMin = Math.min(...arr);
    res = Math.max(currMax, res);
    console.log(currMax, currMin);
  }

  return res;
};
const nums = [2, -5, -2, -4, 3];
console.log(maxProduct(nums));

// 153. Find Minimum in Rotated Sorted Array
/**
 * @param {number[]} nums
 * @return {number}
 */
// O(n)
var findMin = function (nums) {
  return Math.min(...nums);
};
// requirement: O(log(n))=>binary search
var findMin = function (nums) {
  let l = 0,
    r = nums.length - 1,
    res = nums[0];
  //after while, res needs update
  while (l <= r) {
    console.log(res);

    //value of leftmost min, rightmost is also the min
    if (nums[l] < nums[r]) {
      //res store the last elem
      res = Math.min(res, nums[l]);
      break;
    }
    let m = Math.floor((l + r) / 2);
    // res is the lable when dealing with min
    res = Math.min(res, nums[m]);
    if (nums[m] >= nums[l]) {
      l = m + 1;
    } else {
      r = m - 1;
    }
    // console.log(l, r);
    // l++;
    // r--;
  }
  return res;
};
const nums1 = [4, 5, 1, 2, 3];
console.log(findMin(nums1));
// 33. Search in Rotated Sorted Array
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
//O(n)
var search = function (nums, target) {
  let l = 0,
    r = nums.length - 1;
  //= necessary, e.g.[1],1=>the while won't execute
  while (l <= r) {
    if (nums[l] === target) return l;
    if (nums[r] === target) return r;
    l++;
    r--;
  }
  return -1;
};

var search = function (nums, target) {
  let l = 0,
    r = nums.length - 1,
    m = 0;
  //find min
  while (l < r) {
    m = Math.floor((l + r) / 2);

    if (nums[m] >= nums[r]) {
      l = m + 1;
    } else {
      r = m;
    }
  }
  // console.log(l);
  let min = l;
  l = 0;
  r = nums.length - 1;
  //decide direction,setting l,r
  if (target >= nums[min] && target <= nums[r]) {
    l = min;
  } else {
    r = min;
  }
  //ordinary binary search,=single value,e.g.[1],1
  while (l <= r) {
    m = Math.floor((l + r) / 2);
    if (target === nums[m]) {
      return m;
    } else if (target > nums[m]) {
      l = m + 1;
    } else r = m - 1;
  }
  return -1;
};

const nums2 = [3, 1];
target = 3;
console.log(search(nums2, target));
// 15. 3Sum
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// hash method
var threeSum = function (nums) {
  // nums.sort();
  // reliable sort
  nums.sort((a, b) => a - b);
  // console.log(nums);
  let res = [];
  const set = new Set();
  for (let i = 0; i < nums.length; i++) {
    // undefined the first time
    if (nums[i] === nums[i - 1]) continue;
    const map = new Map();
    for (let j = i + 1; j < nums.length; j++) {
      let target = -(nums[i] + nums[j]);
      //tip: convert set value into string, since different obj if not convert
      if (map.has(target) && !set.has(`${[nums[i], nums[j], target]}`)) {
        res.push([nums[i], nums[j], target]);
        set.add(`${[nums[i], nums[j], target]}`);
      }
      map.set(nums[j]);
    }
  }

  return res;
};
// skip tips
var threeSum1 = function (nums) {
  if (nums.length == 0 || nums.length < 3) return [];

  nums.sort((a, b) => a - b);
  console.log(nums);
  // const set = new Set();
  const res = [];
  for (let i = 0; i < nums.length; i++) {
    //fixed i,another [the next value,len-1]
    let low = i + 1,
      high = nums.length - 1;
    while (low < high) {
      const sum = nums[i] + nums[low] + nums[high];

      if (sum === 0) {
        res.push([nums[i], nums[low], nums[high]]);
        //skip duplicate elem
        while (nums[low] === nums[low + 1]) low++;
        while (nums[high] === nums[high - 1]) high--;
        low++;
        high--;
      } else if (sum > 0) {
        high--;
      } else {
        low++;
      }
    }
    while (nums[i] === nums[i + 1]) i++;
  }
  return res;
};
const nums3 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4];
console.log(threeSum(nums3));
// let arr=new Set()
// arr.add([1,1,1])
// arr.add([1,1,1])
// console.log(...new Set(arr))

// 1. Two Sum

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
//hash
var twoSum = function (nums, target) {
  // nums.sort((a,b)=>a-b)
  // console.log(nums)
  const dic = {};
  for (let i = 0; i < nums.length; i++) {
    if (target - nums[i] in dic) {
      return [dic[target - nums[i]], i];
    }
    dic[nums[i]] = i;
  }
  // console.log(dic);
};
const nums4 = [2, 7, 11, 15],
  target1 = 9;
console.log(twoSum(nums4, target1));

//   167. Two Sum II - Input Array Is Sorted
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
//hash
var twoSum = function (numbers, target) {
  const dic = {};
  for (let i = 0; i < numbers.length; i++) {
    if (target - numbers[i] in dic) {
      return [dic[target - numbers[i]] + 1, i + 1];
    }
    dic[numbers[i]] = i;
  }
};
var twoSum = function (numbers, target) {
  let l = 0,
    h = numbers.length - 1;
  while (l < h) {
    // console.log(target, numbers[l], numbers[h]);
    if (target - numbers[l] === numbers[h]) return [l + 1, h + 1];
    else if (target - numbers[l] < numbers[h]) {
    //   console.log(target, h, l);
      h--;
    } else {
      l++;
    //   console.log(h, l);
    }
  }
};
const numbers = [2, 7, 11, 15],
  target2 = 18;
console.log(twoSum(numbers, target2));
