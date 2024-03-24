#include <iostream>
#include <vector>
#include <string>

using namespace std; // for convenience

class Solution {
  public:
    string encode(vector<string>& strs) {
      string res;
      for (int i = 0; i < strs.size(); i++) {
        res += to_string(strs[i].size()) + "#" + strs[i];
      }
      return res; // need to return a string here
    }

    vector<string> decode(string s) {
      int i = 0;
      vector<string> result;

      while (i < s.size()) {
        int j = i;
        while (j < s.size() && s[j] != '#') {
          j++;
        }

        int str_len = stoi(s.substr(i, j - i));
        string word = s.substr(j + 1, str_len);
        result.push_back(word);

        i = j + 1 + str_len; // Move to the next token
      }
      return result;
    }
};

int main() {
  Solution ncdr_dcdr; // corrected object declaration
  vector<string> input = {"neet", "code", "love", "you"}; // input data
  std::cout << ncdr_dcdr.encode(input); // calling encode on ncdr_dcdr object

  return 0;
}
