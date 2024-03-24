class Solution {
  encode = (lst) => lst.length === 0 
    ? [] : lst.length === 1
    ? [lst] : lst.join('');
  decode = (str) => str.length === 0 
    ? [] : str.length === 1
    ? [str] : str.split('');
}

const soln = new Solution();
let testcase1 = ["neet","code","love","you"];
let testcase2 = [""];
let joined = soln.encode(testcase1);

console.log(joined);
console.log(soln.decode(joined));
