"""
    两个方法。第二个方法是某大神的。只用了4行。
    第一个方法参考了大神的解法。
    主要在于理解
"""

# 方法一
class Solution:
    def romanToInt(self, s: str)->int :
        d = {'I':1, 'IV':3, 'V':5, 'IX':8,
             'X':10, 'XL':30, 'L':50, 'XC':80,
             'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        sum = 0
        for i,n in enumerate(s):
            a = d.get(s[max(i-1,0):i+1],d[n])
            sum = sum + a
        return sum
        
p=Solution()
print(p.romanToInt("MCMXCIV"))


#方法二
class Solution1:
    def romanToInt1(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8,
             'X':10, 'XL':30, 'L':50, 'XC':80,
             'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))


p1=Solution1()
print(p1.romanToInt1("IX"))
