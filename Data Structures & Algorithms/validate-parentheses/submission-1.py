class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        st = []
        for i in s:
            if i=='(' or i=='[' or i =='{':
                st.append(i)
            else:
                if st and st[-1] == valid.get(i,0):
                    st.pop()
                else:
                    return False
        if st:
            return False
        return True


        
        