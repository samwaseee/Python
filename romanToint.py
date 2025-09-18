class Solution:
    def romanToInt(self, s: str) -> int:
        for i, j in (("IV", "IIII"), ("IX", "VIIII"), ("XL", "XXXX"), ("XC", "LXXXX"), ("CD", "CCCC"), ("CM", "DCCCC")):
            s = s.replace(i, j)
        return sum({"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[c] for c in s)# Example usage:
sol = Solution()  
print(sol.romanToInt("MCMXCIV"))