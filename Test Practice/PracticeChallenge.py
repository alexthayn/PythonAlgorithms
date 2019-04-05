
def solution(max):
    if max < 2:
        return 0
    num1 = 1
    num2 = 2
    sum = 0

    i = 0
    while(num2 < max):
        if(num2 % 2 == 0):
            sum += num2
            print(sum)

        next = num1 + num2
        num1 = num2
        num2 = next
        i += 1

    return sum


# solution(2)
# solution(5)
# solution(100)


def binTreeSolution(arr):
    if(len(arr) == 0):
        return ""

    levels = []
    levels.append([arr[0]])

    levelNum = 1
    i = 1
    # populate each level with node values
    # Suppose you're given a binary tree represented as an array. For example, [3,6,2,9,-1,10] represents the following binary tree where -1 is a non-existent node):

    while i < len(arr):
        currLevel = []
        upperLevelIter = 0

        while len(currLevel) < 2**levelNum and i < len(arr):
            if levels[levelNum-1][upperLevelIter] == -1:
                currLevel.append(-1)
            else:
                currLevel.append(arr[i])
            i += 1
            if(i % 2 == 1):
                upperLevelIter += 1

        levelNum += 1
        levels.append(currLevel)

    leftBranch = 0
    rightBranch = 0
    for level in range(1, len(levels)):
        halfMark = int(2 ** level / 2)
        if len(levels[level]) <= halfMark:
            for value in levels[level]:
                if(value > 0):
                    leftBranch += value
        else:
            for value in levels[level][:halfMark]:
                if(value > 0):
                    leftBranch += value
            for value in levels[level][halfMark:]:
                if(value > 0):
                    rightBranch += value

    print(levels)

    if leftBranch == rightBranch:
        return ""
    return "Left" if leftBranch > rightBranch else "Right"


print(binTreeSolution([3, 6, 2, 9, -1, 10]))
print(binTreeSolution([3]))
print(binTreeSolution([3, 6, 12]))

binTreeSolution([3, 6, 2, 9, -1, 10, 2, 5, 6, 7,
                 8, 2, 4, 5, 4, 3, 56, 3, 6, 2])


def test_binTreeSolution():
    assert binTreeSolution([3, 6, 2, 9, -1, 10]) == "Left"
    assert binTreeSolution([3]) == ""
    assert binTreeSolution([3, 2, 10]) == "Right"
    assert binTreeSolution(
        [3, 2, 3, 56, -1, 4, 2, 1, 3, 4, 6, 7, 5, 4, 3, 2]) == "Left"
