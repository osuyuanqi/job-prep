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
    let l = 0;
    (r = nums.length - 1), (m = 0);
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
    //ordinary binary search
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
  
  const nums2 = [ 5,6,7,1,2,3,4],
    target = 4;
  console.log(search(nums2, target));
  