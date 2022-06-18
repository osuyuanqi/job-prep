// 169. Majority Element
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let dic = {},
    count = 0;
  for (let i of nums) {
    if (i in dic) {
      dic[i]++;
    } else {
      dic[i] = 1;
    }
  }
  console.log(dic);
  let res = [-Infinity, -Infinity];
  for (const [k, v] of Object.entries(dic)) {
    // console.log(k, v);
    if (v > res[1]) {
      res[0] = k;
      res[1] = v;
    }
  }
  return res[0];
};
const nums = [3, 2, 3];
console.log(majorityElement(nums));
// 217. Contains Duplicate
/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function (nums) {
    const set = new Set();
    for (let i of nums) {
      if (set.has(i)) {
        return true;
      } else {
        set.add(i);
      }
    }
    return false;
  };
  const nums1 = [1, 2, 3];
  console.log(containsDuplicate(nums1));
  // 242. Valid Anagram
  /**
   * @param {string} s
   * @param {string} t
   * @return {boolean}
   */
  //hash
  var isAnagram = function (s, t) {
    //s,t is string, use 'of' to iterate
    // dic is obj, use 'in' to iterate
    if (s.length !== t.length) return false;
    const dic = {};
    for (const i of s) {
      if (i in dic) {
        dic[i]++;
      } else {
        dic[i] = 1;
      }
    }
    console.log(dic);
    for (const i of t) {
      if (i in dic) {
        dic[i]--;
      } else return false;
    }
    console.log(dic);
    //change parameter to k
    for (const k in dic) {
      console.log(dic[k], k);
      if (dic[k] !== 0) return false;
    }
    return true;
  };
  
  var isAnagram = function (s, t) {
    if (s.length !== t.length) return false;
    const dic = {};
    for (const i of s) {
      if (i in dic) dic[i]++;
      else dic[i] = 1;
    }
    console.log(dic);
    for (const j of t) {
      // if (j in dic) {
      //0==false
      if (!dic[j]) return false;
      // to 0->never came again
      else dic[j]--;
    }
    return true;
  };
  const s = "aba",
    t = "baa";
  console.log(isAnagram(s, t));
  