/* **********************************************
 * 62. Unique Paths
 ************************************************/

/**********************************************
 * 20. Valid Parentheses
 * @param {string} s
 * @return {boolean}
 **********************************************/
// built-in replace
var isValid = function(s) {
    for(let i in s){
        s=s.replace("[]","").replace("{}","").replace("()","");
        if (s=="")
            return true;
    }
    return false;
};
// 
var isValid = function(s) {
    if (s.length%2!=0) return false;
    const dic={"{":"}","(":")","[":"]"};
    const stack =[]
    for(let i of s){
        // all left parentheses have been added here
        if (i=="{"||i=="("||i=="["){
            stack.push(i);
        }
        // pop the last elem
        else if (stack!=null&&i!=dic[stack.pop()]){
            return false;
        }
    }
    return stack=="";
};
// var s="()"
// console.log(isValid(s))

// 28. Implement strStr()
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
// way1: substring
var strStr = function(haystack, needle) {
    // ask interviewer the empty issue
    if (needle=="") return 0;
    let remainLen=haystack.length-needle.length
    // +1, need to familiarize for loop
    for (let i=0;i<remainLen+1;i++){
        // console.log(i,haystack.substring(i,i+needle.length))
        if (haystack.substring(i,i+needle.length)==needle)
            return i
    }
    return -1
};
// way2: built-in indexOf
var strStr=function (haystack,needle) {
    return haystack.indexOf(needle);
}

// let haystack = "hello", needle = "ll"
// console.log(strStr(haystack,needle))


// 160. Intersection of Two Linked Lists
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
// math:a+b+c=a+c+b
var getIntersectionNode = function(headA, headB) {
    let p1=headA,p2=headB;
    while (p1!=p2){
        // headA and headB stay at the original position
        p1=p1==null?headB:p1.next;
        p2=p2==null?headA:p2.next;
    }
    return p2
};

// hash set
var getIntersectionNode = function(headA, headB) {
    const set=new Set()
    while(headA){
        set.add(headA)
        headA=headA.next
    }
    while(headB){
        if (set.has(headB)){
            return headB
        }
        headB=headB.next
    }
};