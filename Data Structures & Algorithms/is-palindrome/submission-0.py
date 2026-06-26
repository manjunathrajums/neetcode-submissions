class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in s:
            if i.isalnum():
                new_string += i.lower()
        if new_string == new_string[::-1]:
            return True
        return False



        