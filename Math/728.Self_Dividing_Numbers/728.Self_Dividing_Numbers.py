class Solution: 
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            if '0' not in str(i) and all([i % int(digits) == 0 for digits in str(i)]):
                result.append(i)
        return result
