# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
#
# Example 1:
from PIL import Image
im = Image.open('img/img.png')
im.show()
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# SOLUTION I (using lists)
def TrappingRainWater(points):
    for i, val in enumerate(points):
        if val > 0:
            first_edge = val
            first_edge_index = i
            break

    end = False
    total_water = 0
    new_list = points[first_edge_index + 1:]

    print(new_list)
    print('         ')

    while end == False:

        fill_sum = 0

        if max(new_list) >= first_edge:

            for i, val in enumerate(new_list):

                if val >= first_edge:
                    second_edge = val
                    second_edge_index = i

                    for value in new_list[:second_edge_index]:
                        fill_sum += value
                    water = min(first_edge, second_edge) * second_edge_index - fill_sum
                    total_water += water

                    # new edge found, changing first_edge_index
                    first_edge = val
                    first_edge_index = i

                    new_list = new_list[first_edge_index + 1:]

                    break

        else:
            second_edge = max(new_list)
            second_edge_index = new_list.index(second_edge)

            for value in new_list[:second_edge_index]:
                fill_sum += value
            water = second_edge * second_edge_index - fill_sum
            total_water += water

            first_edge = second_edge
            first_edge_index = second_edge_index

            new_list = new_list[first_edge_index + 1:]

        if len(new_list) <= 2:
            end = True

    return 'The whole Trapping Rain Water : ', total_water




