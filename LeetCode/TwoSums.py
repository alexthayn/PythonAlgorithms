# https://leetcode.com/problems/two-sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap to search for values quickly
        hashMap = {}
        i = 0
        for num in nums:
            hashMap[num] = i
            i+=1
        
        for i in range(len(nums)):
            targetValue = target - nums[i]
            print("target value: %d"%(targetValue))
            if targetValue in hashMap.keys() and hashMap[targetValue] != i:
                print(hashMap[targetValue])
                print(i)
                return [i,hashMap[targetValue]]
            
        return None


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([1,4,5,6,7], 9))

################## TESTS ##################
test = Solution()

def test_TwoSumNoAnswer():

    assert test.twoSum([],0) == None
    assert test.twoSum([0,0,0], -204) == None

def test_TwoSumWithAnswers():
    assert test.twoSum([1,2,3], 5) == [1,2]
    assert test.twoSum([1,5,5,11],10) == [1,2]
    assert test.twoSum([-10,-2,-6,3],-3) == [2,3]