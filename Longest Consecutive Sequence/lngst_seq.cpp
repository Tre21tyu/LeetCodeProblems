#include <iostream>
#include <vector>
#include <set>

class Solution {
  public:
    int longestConsecutive(vector<int>& nums) {
      std::set<int> st(nums.begin(), nums.end());
      int st_len = st.size();  
      int ans = 0;    
      for (int i = 0; i < nums.size(); i++) {
        int num_one_less = nums[i] - 1;
        auto in_set = st.find(num_one_less);
        if (in_set != st.end()) { continue; }
        int j = 0;
        while (j != st_len) {
          int num_one_more_j = nums[i] + 1 + j;
          auto in_set_ = st.find(num_one_more_j);
          if (in_set_ != st.end()) {
            j++;
          }
          else { break; }
          if (j + 1 > ans) { ans = j + 1; }
        }
      }
      return ans;
    }
};
