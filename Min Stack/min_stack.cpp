#include <stack>
#include <algorithm>

class MinStack {
  private:
    std::stack<int> stack;
    std::stack<int> min_stack;

  public:
    MinStack() {}

    void push(int val) {
      stack.push(val);
      if (min_stack.empty() || val <= min_stack.top()) {
        min_stack.push(val);
      }
    }

    void pop() {
      if (!stack.empty()) {
        if (stack.top() == min_stack.top()) {
          min_stack.pop();
        }
        stack.pop();
      }
    }

    int top() {
      return stack.empty() ? 0 : stack.top();
    }

    int getMin() {
      return min_stack.empty() ? 0 : min_stack.top();
    }
};
