/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // Create a Set to store unique elements
    let uniqueSet = new Set();

    // Iterate through the array
    for (let num of nums) {
        // If the element is already in the set, it's a duplicate
        if (uniqueSet.has(num)) {
            return true;
        }
        
        // Otherwise, add it to the set
        uniqueSet.add(num);
        console.log(uniqueSet);
    }

    // No duplicates found
    return false;
};

console.log(containsDuplicate([2, 3, 4, 3]))