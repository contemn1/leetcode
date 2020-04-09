class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        extra = 0
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        diff = len(num2) - len(num1)
        existing_result = ""
        for i in range(-1, -len(num1) -1, -1):
            
            current = int(num1[i]) + int(num2[i]) + extra
            
            if current > 10:
                current = current % 10
                extra = 1
            else:
                extra = 0
            
            existing_result = str(current) + existing_result
        
        if diff == 0:
            prefix = extra
        else:
            prefix = int(num2[:diff]) + extra
        return existing_result if prefix == 0 else str(prefix) + existing_result
        
if __name__ == "__main__":
    a = Solution()
    a.addStrings("2332", "3181")