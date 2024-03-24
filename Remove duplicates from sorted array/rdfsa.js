/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let lp = 1;
  for (let rp = 1; rp < nums.length; rp++) {
    if (nums[rp] !== nums[rp - 1]) {
      nums[lp] = nums[rp];
      lp++;
    }
  }
  nums.length = lp;
  return [lp, nums];
};

console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
console.log(removeDuplicates([1, 1, 2, 3, 4, 5, 5, 5]))
