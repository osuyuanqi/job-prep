/**190. Reverse Bits
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  // console.log()
  let b = n.toString(2);
  // console.log(b)
  let a = b.padStart(32, "0");
  // console.log(a);supplement 0
  let rev = a.split("").reverse().join("");
  return parseInt(rev, 2);
};

// 125. Valid Palindrome
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const a = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  return a.split("").reverse().join("") === a;
};
// let s = "A man, a plan, a canal: Panama";
// console.log(isPalindrome(s));

// 189. Rotate Array
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (numsa, k) {
  const newK = k % nums.length;
  let newA = nums.splice(-newK);
  nums.splice(0, 0, ...newA);
};
// (nums = [1, 2, 3, 4, 5, 6, 7]), (k = 3);
// rotate(nums, k);
// console.log(nums);

// 7. Reverse Integer
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const sign = x > 0 ? 1 : -1;
  let a = x * sign;
  let b = a.toString().split("").reverse().join("");
  let res = sign * parseInt(b);
  return res > (-2) ** 31 && res < 2 ** 31 - 1 ? res : 0;
};

var reverse = function (x) {
  const sign = x > 0 ? 1 : -1;
  let a = x * sign;
  ([res,c])=([0,0])
  while (a) {
     res = a % 10+res*10;
    a=Math.floor(a/10);
    console.log(res,a);
  }
  res *= sign;
  return res > (-2) ** 31 && res < 2 ** 31 - 1 ? res : 0;
};

// const x = -123;
// console.log(reverse(x));

// 344. Reverse String
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
// built-in function
var reverseString = function(s) {
  s.reverse().join("");
};
// swap
var reverseString = function(s) {
  let l=0,r=s.length-1;
  while (l<r){
    [s[l],s[r]]=[s[r],s[l]]
    l++;
    r--;
  }
};
// s = ["h","e","l","l","o",'a'];
// reverseString(s);
// console.log(s);

// 94. Binary Tree Inorder Traversal
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
// recursieve
 var inorderTraversal = function(root) {
  const res=[];
  const rev=function(r){
      if (r==null){
          return;
      }
      rev(r.left);
      res.push(r.val);
      rev(r.right);
  }
  rev(root);
  return res;
};
//iterative
var inorderTraversal = function(root) { 
  const stack=[],res=[];
  let curr=root;
  //stack.length===0, means false
  while (root!=null||stack.length){
      while (root!=null){
          stack.push(root);
          root=root.left;
      }
      curr = stack.pop();
      res.push(curr.val);
      //finish one branch first
      root=curr.right
  }
  return res;
}

// 204. Count Primes
/**
 * @param {number} n
 * @return {number}
 */
 var countPrimes = function (n) {
  if (n < 3) return 1;
  let res = 0;
  //   let half = Math.floor(Math.sqrt(n));
  let half = n;
  console.log(half);
  for (let i = 3; i < half; i++) {
    // if
    let isPri = true;
    for (let j = 2; j < i; j++) {
      if (i % j === 0) isPri = false;
    }
    // console.log(isPri);
    if (isPri) res++;
  }
  return res + 1;
};
// console.log(countPrimes(8));

// method2: check half, but use n
function isPri(n) {
  let checkPri = true;
  let half = Math.floor(Math.sqrt(n)) + 1;
  console.log(half);
  for (let j = 2; j < half; j++) {
    // use n-> the original value
    if (n % j === 0) {
      checkPri = false;
      break;
    }
  }
  return checkPri;
}

var countPrimes = function (n) {
  //   let res = 0,arr=[0]*n;
  if (n < 3) return 1;
  let res = 0;
  for (let i = 3; i < n; i++) {
    if (isPri(i)) res++;
  }
  return res + 1;
};

//way3: dynamic programming
var countPrimes = function (n) {
  if (n < 3) return 0;
  let arr = new Array(n).fill(1);
  arr[0]=arr[1]=0;
  for(let i=2;i*i<n;i++){
      if(!arr[i]){continue;}
      for(let j=i*i;j<n;j+=i){
          arr[j]=0;
      }
  }
  console.log(arr);
  return arr.reduce(((a,b)=>a+b));
};

// console.log(countPrimes(8));
