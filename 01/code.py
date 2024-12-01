import numpy as np

# part 1

# load the input
input = np.loadtxt('input.txt', dtype=int)

# assign two empty lists
leftList = []
rightList = []

# iterate over the input, assigning the first index of each subarray
# into the leftList  and the second index to the rightList

for arr in input:
    leftList.append(arr[0])
    rightList.append(arr[1])

# sort both lists
leftList.sort()
rightList.sort()

# assign result list
resultList = []

# compare each index of leftList with rightList
for left, right in zip(leftList, rightList):

    if right > left:
        diff = right - left
    else:
        diff = left - right

    resultList.append(diff)

result = sum(resultList)
print(result)

# part 2

similarityScore = 0

# if leftList number appears x times in rightList multiply leftList number by x
for num in leftList:
    occurences = rightList.count(num)
    if occurences > 0:
        score = occurences * num
        similarityScore = similarityScore + score
    else:
        continue

print(similarityScore)
