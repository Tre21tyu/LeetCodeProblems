#include <iostream>
#include <vector>
#include <iterator> // Added to include std::ostream_iterator

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> ans(n);
        std::vector<int> left_Product(n);
        std::vector<int> right_Product(n);
        left_Product[0] = 1;
        for(int i=1; i<n; i++){
            left_Product[i] = left_Product[i-1] * nums[i-1];
        }
        right_Product[n-1] = 1;
        for(int i=n-2; i>=0; i--){
            right_Product[i] = right_Product[i+1] * nums[i+1];
        }
        for(int i=0; i<n; i++){
            ans[i] = left_Product[i] * right_Product[i];
        }
        return ans;
    }
};

void printVector(const std::vector<int>& vec) {
    std::copy(vec.begin(), vec.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;
}

int main() {
    Solution solution;
    std::vector<int> test_nums = {1,2,3,4};
    std::vector<int> result = solution.productExceptSelf(test_nums);
    printVector(result);
    return 0;
}
