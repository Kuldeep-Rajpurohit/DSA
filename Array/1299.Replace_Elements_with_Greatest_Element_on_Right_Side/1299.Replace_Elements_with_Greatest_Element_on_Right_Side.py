class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        prev = arr[-1]
        arr[-1] = -1
        while i >= 0:
            largest = max(prev, arr[i+1])
            prev = arr[i]
            arr[i] = largest
            i -= 1
        return(arr)
