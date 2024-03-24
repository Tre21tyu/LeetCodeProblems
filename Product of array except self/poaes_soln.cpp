#include <iostream>
#include <vector> // Include the vector header

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);
        int prefix = 1;
        for (int i = 0; i < nums.size(); ++i) {
            result[i] *= prefix;
            prefix *= nums[i];
        }
        int suffix = 1;
        for (int i = nums.size() - 1; i >= 0; --i) {
            result[i] *= suffix;
            suffix *= nums[i];
        }
        return result;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 1, 2, 3}; // Sample vector
    vector<int> result = solution.productExceptSelf(nums); // Call the method to calculate product except self
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
