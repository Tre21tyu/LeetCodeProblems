class Solution {
  public:
    int removeDuplicates(vector<int>& nums) {
      int lp = 1;
      for (int rp = 1; rp < nums.size(); rp++) {
        if (nums[rp] != nums[rp - 1]) {
          nums[lp] = nums[rp];
          lp++;
        }
      }       
      return lp;
    }
};
