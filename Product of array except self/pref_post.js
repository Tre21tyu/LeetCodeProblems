/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  let start = 1;
  let prefix_list = [];
  for (let i = 0; i < nums.length; i++) {
    prefix_list[i] = start;
    start *= nums[i];
  }
  
  let post_start = 1;
  let postfix_list = [];
  for (let i = nums.length - 1; i > -1; i--) {
    postfix_list[i] = post_start;
    post_start *= nums[i];
  }

  let result = []
  for (let i = 0; i < nums.length; i++) {
    result.push(prefix_list[i]*postfix_list[i])
  }

  return [prefix_list, postfix_list]
  // return result;
};

console.log(productExceptSelf([1, 2, 3, 4]));
