class Solution:
    def defangIPaddr(self, address: str) -> str:
        addre = list(address.split("."))
        output = "[.]".join(addre)
        return output
