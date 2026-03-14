class Solution:
    def defangIPaddr(self, address: str) -> str:
        print(len(address))


sol = Solution()
address = "1.1.1.1"
# address = "255.100.50.0"
result = sol.defangIPaddr(address)
print(result)
