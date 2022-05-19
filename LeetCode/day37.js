/**190. Reverse Bits
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
 var reverseBits = function(n) {
  // console.log()
     let b =n.toString(2)
     // console.log(b)
     let a=b.padStart(32,'0')
     // console.log(a);supplement 0
     let rev=a.split('').reverse().join('')
     return parseInt(rev,2)
 };