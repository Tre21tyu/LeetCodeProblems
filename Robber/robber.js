var rob = function(nums) {
    let max = Math.max(...nums);
    let profits = [];
    let final = 0;

    profits.push(max);
    if (nums.length > 3) {
        let index = nums.indexOf(max);
        let nextIndex = (index + 2) % nums.length;
        let hops = Math.floor(nums.length / 2) - 1;
        for (let i = 0; i < hops; i++) {
            profits.push(nums[nextIndex + (i * 2)]);
        }
        for (let i = 0; i < profits.length; i++) {
            final += profits[i];
        }
        return final;
    }
    return max;
}

console.log(rob([2, 3, 4, 5, 9]))