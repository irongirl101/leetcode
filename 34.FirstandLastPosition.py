# binary searchhh 

nums = [5,7,7,8,8,10]
target = 7

def search(arr, target):
    low = 0 
    high = len(nums) - 1
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Check if the target is present at the mid index
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
            
        # If target is smaller, ignore the right half
        else:
            high = mid - 1
            
    # Target element was not present in the list
    return -1

result = search(nums,target)

if result == -1: 
    print([-1,-1])
else: 
    print([result-1,result])