def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)
        for i in range(n-2):
            left = i+1
            right = n-1
            
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total == target:
                    return True
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return False

# Example usage
arr = [1, 2, 3, 4, 5]
target = 9
print(hasTripletSum(None, arr, target))  # Output: True (1 + 3 + 5 = 9)