using namespace std; // Add this line to use std namespace

class Solution {
  private:
    stack<int> stack; // Use int type for the stack since RPN expressions only involve integers

  public:
    int evalRPN(vector<string>& tokens) {
      for (const auto& token : tokens) {
        try {
          int operand = stoi(token); // Convert the token to an integer operand
          stack.push(operand); // Push the operand onto the stack
        }
        catch (const invalid_argument& e) {
          // Handle operator tokens
          int x = stack.top(); stack.pop(); // Pop the top element (second operand)
          int y = stack.top(); stack.pop(); // Pop the next top element (first operand)
          int res;

          // Perform the operation based on the operator token
          if (token == "+") {
            res = y + x;
          }
          else if (token == "-") {
            res = y - x;
          }
          else if (token == "*") {
            res = y * x;
          }
          else if (token == "/") {
            res = y / x; // Note: Integer division is used here
          }

          stack.push(res); // Push the result back onto the stack
        }
      }

      return stack.top(); // Return the top element of the stack as the final result
    }
};
