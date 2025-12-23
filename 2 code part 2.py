# 22. Generate Parentheses
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8


def generateParenthesis(n):
    res = []

    def bt(curr="",open_count=0,close_count=0):
        if (len(curr))== 2*n:
            res.append(curr)
            return
        
        if open_count < n:
            bt(open_count + 1, close_count, curr + "(")

        if close_count < open_count:
            bt(open_count, close_count + 1, curr + ")")

    bt(0,0 "")
    return res