class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_string):
            # If length matches digits, we found a valid combination
            if index == len(digits):
                result.append(current_string)
                return
            
            # Try all letters corresponding to the current digit
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, current_string + letter)
                
        backtrack(0, "")
        return result
        