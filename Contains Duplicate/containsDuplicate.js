/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let seen_nums = {};

    for (let i = 0; i < nums.length; i++) {
        // Use "in" operator to check if the key exists in seen_nums
        if (nums[i] in seen_nums) {
            return true;
        } 
        else {
            seen_nums[nums[i]] = true; // You can set any value, e.g., true
        }
    }
    return false;
};

console.log(containsDuplicate([1, 2, 3]));