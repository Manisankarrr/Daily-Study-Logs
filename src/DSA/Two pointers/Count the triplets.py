class Solution:
    # Given an array of integers, count the number of triplets such that the sum of any two elements equals the third element.
    # Example: arr = [1, 5, 3, 2], triplets are (1,2,3) and (2,3,5), so output is 2.
    def countTriplet(self, arr):
        arr.sort()
        count = 0
        for i in range(2, len(arr)):
            low = 0
            high = i - 1
            while low < high:
                val = arr[low] + arr[high]
                if val == arr[i]:
                    count += 1
                    low += 1
                    high -= 1
                elif val < arr[i]:
                    low += 1
                else:
                    high -= 1
        return count

# Example usage:
if __name__ == "__main__":
    arr = [1, 5, 3, 2]
    sol = Solution()
    print(sol.countTriplet(arr))  # Output: 2
