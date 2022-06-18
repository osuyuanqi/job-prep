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
