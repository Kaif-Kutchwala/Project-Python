
def maxArea(heights : list[int]) -> int:
    leftPointer = 0                     # can be thought of as leftIndex
    rightPointer = len(heights) - 1     # can be thought of as rightIndex
    maxArea = 0

    while leftPointer < rightPointer:
        area = (rightPointer - leftPointer) * min(heights[leftPointer], heights[rightPointer])
        maxArea = max(maxArea, area)
        
        if heights[leftPointer] < heights[rightPointer]:
            leftPointer += 1  # leftIndex = leftIndex + 1
        else:
            rightPointer -= 1  # rightIndex = rightIndex - 1

    return maxArea

def maxAreaBruteForce(heights: list[int]) -> int:
    maxArea = 0
    for leftIndex in range(len(heights)):
        for rightIndex in range(leftIndex, len(heights)):
            area = (rightIndex - leftIndex) * min(heights[leftIndex], heights[rightIndex])
            maxArea = max(area, maxArea)
    return maxArea


print(maxArea([1,6,8,2,5,4,8,3,7]))     # 42
print(maxArea([3,5,2,8,10,1,6]))        # 25
print(maxArea([4,12,6,3,9,2,2,1,5]))    # 35
print(maxArea([9,8,9,3,6,2,1,5,7]))     # 56