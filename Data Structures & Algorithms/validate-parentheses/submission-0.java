class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            // System.out.println(stk);
            if (stk.size() == 0) {
                stk.push(s.charAt(i));
                continue;
            }
            if (stk.peek() == '(' && s.charAt(i) == ')') {
                stk.pop();
            }
            else if (stk.peek() == '{' && s.charAt(i) == '}') {
                stk.pop();
            }
            else if (stk.peek() == '[' && s.charAt(i) == ']') {
                stk.pop();
            }
            else {
                stk.push(s.charAt(i));
            }
        }
        if (stk.size() == 0) {
            return true;
        }
        else {
            return false;
        }
    }
}
