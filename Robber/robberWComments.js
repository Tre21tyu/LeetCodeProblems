var rob = function(nums) {
    let max = Math.max(...nums);
    let profits = [];
    let final = 0;

    profits.push(max);
    if (nums.length > 3) {
        let index = nums.indexOf(max);
        let nextIndex = (index + 2) % nums.length;
        let hops = Math.floor(nums.length / 2)
        for (let i = 0; i < hops; i++) {
            profits.push(nums[nextIndex + (i * 2)]);
            // console.log();         
            // console.log("-----------")
            // console.log(`nextIndex + i = ${nextIndex} + ${i} = ${nextIndex + i}`);
            // console.log(`nums: ${nums}`)
            // console.log(`nums @ nextIndex + i = nums @ ${nextIndex} + ${i} = nums[${nextIndex} + ${i}] = ${nums[nextIndex + (i)]}`)
            // console.log("-----------")   
            // console.log();            
            // console.log();         
            // console.log("-----------")
            // console.log(`nextIndex + i * 2 = ${nextIndex} + ${i} * 2 = ${nextIndex + (i * 2)}`);
            // console.log(`nums: ${nums}`)
            // console.log(`nums @ nextIndex + i * 2 = nums @ ${nextIndex} + ${i} * 2 = nums[${nextIndex} + ${i * 2}] = ${nums[nextIndex + (i * 2)]}`)
            // console.log("-----------")   
            // console.log();
            
            // console.log("-----------")
            // console.log(nums[nextIndex + (2 * i)])
            // console.log("-----------")
            // console.log(nums[nextIndex + (i)])
            // console.log("-----------")
            // console.log(profits)
            // console.log("-----------")
            // console.log("-----------")
            // console.log()
            // console.log()
        }
        for (let i = 0; i < profits.length; i++) {
            final += profits[i];
        }
        return final;
    }
    return max;
}

console.log(rob([3,1,4,6,5]))

