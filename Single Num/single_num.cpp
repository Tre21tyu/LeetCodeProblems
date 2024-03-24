#include <iostream>
#include <vector>

class Solution {
  public:
    int singleNumber(vector<int>& nums) {
      xor = 0;
      for (int i = 0; i < nums.size(); i++) {
        xor ^= nums[i];
      }
      return xor;
    }
}
