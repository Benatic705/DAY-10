# Problem 1 - Two Sum
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Two Sum:", [i, j])

# Problems 2 - Palindrome Number
num = 121

if str(num) == str(num)[::-1]:
    print("Palindrome")

# Problem 3 - Contains Duplicate
nums = [1,2,3,1]

if len(nums) != len(set(nums)):
    print("Duplicate Found")

# Problem 4 - Binary Search
nums = [1, 2, 3, 4, 5]
target = 4

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Binary Search Found:", mid)
        break

    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Problem 5 - Maximum Number
nums = [5,10,15,20]
print("Maximum:", max(nums))

# Problem 6 - Minimum Number
print("Minimum:", min(nums))

#Problem 7 - Reverse String
text = "Python"
print("Reversed:", text[::-1])

# Problem 8 - Sum of Array
nums = [ 1,2,3,4,5]
print("Sum:", sum(nums))

# Problem 9 - Count Elements
print("Count:", len(nums))

#promblem 10 - Sort Array
nums = [5,2,8,1]
nums.sort()
print("Sorted:", nums)