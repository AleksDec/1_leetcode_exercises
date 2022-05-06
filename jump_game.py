#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#The goal is to reach the last index in the minimum number of jumps.
#Assume that you can always reach the last index.
#
#Example 1:
#Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.


def min_jumps(list_of_numbers):
  nums = list_of_numbers
  pos = 0
  jump = 0
  end = False

  while end == False:
    step_num_sum = 0

    for i in range (1,nums[pos]+1):
      step = i
      # find the biggest 'jump + number' -> jump_num_sum
      if pos + step >= len(nums) - 1:
        end = True
      elif step + nums[pos + step] >= step_num_sum :
        step_num_sum = step + nums[pos + step]
        new_pos = pos + step

    jump += 1
    pos = new_pos

  return jump

if __name__ == '__main__':
    numbers = input("Your list of numbers : ")
    numbers = numbers.strip('[]').replace(',', '')
    numbers_int = [int(el) for el in numbers]
    print(min_jumps(numbers_int))