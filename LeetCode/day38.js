// 680. Valid Palindrome II
/**
 * @param {string} s
 * @return {boolean}
 */
// way1: consider odd and left
var validPalindrome = function (s) {
  let l = 0,
    r = s.length - 1;
  let arr = [];
  // res = 0;
  while (l < r) {
    if (s[l] !== s[r]) {
      // even:abccda,compare bccd
      let even = s.substring(l, r);
      // odd: move right totally, pass one and compare right. e.g.abdeaedca->deaedc or bdeaed
      // exclude end
      let odd = s.substring(l + 1, r + 1);
      return (
        even === even.split("").reverse().join("") ||
        odd === odd.split("").reverse().join("")
      );
    }
    l++;
    r--;
  }
  return true;
};
// way2: move left and right explaination
function isPar(s) {
  // console.log(s)
  return s === s.split("").reverse().join("");
}
var validPalindrome = function (s) {
  let l = 0,
    r = s.length - 1;
  let arr = [];
  // res = 0;
  while (l < r) {
    if (s[l] !== s[r]) {
      // move right, skip l->[l+1,r+1) ;or move left, skip r->[l,r)
      // console.log(s[l],s[r])
      return isPar(s.substring(l + 1, r + 1)) || isPar(s.substring(l, r));
    }
    l++;
    r--;
  }
  return true;
};
// const s = "aeab";
// console.log(validPalindrome(s));

// 2108. Find First Palindromic String in the Array
/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function (words) {
  let res = "";
  //   res = words.forEach((word) => {
  //       console.log(word);
  //     if (word === word.split("").reverse().join(""))
  //     {return word;}

  //   });
  for (let i = 0; i < words.length; i++) {
    if (words[i] === words[i].split("").reverse().join("")) {
      res = words[i];
      return res;
    }
  }
  return res;
};
// filter
var firstPalindrome = function (words) {
  let res = "";
  res = words.filter((word) => {
    if (word === word.split("").reverse().join("")) {
      return word;
    }
  });
  console.log(res);
  return res.length > 0 ? res[0] : "";
};
// performance improvemant: cal half
var firstPalindrome = function (words) {
  let res = "";
  for (const word of words) {
    let isP = true;
    for (let i = 0; i < Math.floor(word.length / 2); i++) {
      if (word[i] !== word[word.length - i - 1]) {
        // console.log(word[i],word[word.length-i-1])
        isP = false;
        break;
      }
    }
    if (isP) {
      res = word;
      break;
    }
  }
  return res;
};
// const words = ["ded", "ghi"];
// console.log(firstPalindrome(words));
