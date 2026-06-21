def twoSum(numbers, target):
    savedElements = {}

    for i, number in enumerate(numbers):
        difference = target - number
        if difference in savedElements:
            return [savedElements[difference], i]
        savedElements[number] = i 

answer = twoSum([1,5,3,4],3)
print(answer)