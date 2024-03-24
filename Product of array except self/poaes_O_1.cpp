#include <iostream>
#include <vector>
#include <iterator> // Added to include std::ostream_iterator

class Solution {
  public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
      int n = nums.size();
      std::vector<int> ans(n);
      std::vector<int> output(n);

      output[0] = 1;
      for(int i=1; i<n; i++){
        output[i] = output[i-1] * nums[i-1];
      }
      int right = 1;
      for (int i = n-1; i >= 0; i--) {
        output[i] *= right;
        right *= nums[i];
      }
      return output;
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
