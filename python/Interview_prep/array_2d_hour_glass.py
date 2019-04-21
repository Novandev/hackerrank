"""
2D Array - DS

THis function should take a random 6x6 array and postion wise get a sum of all of the elements in the
"""
import traceback

def hourglass_max_sum(d_array: list) -> int:
    """
    Params: an array that is a 6X6
    Return: a max value of the patern defined in the array
    """
    # print(d_array)
    hour_glass =[ [0,0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2,2] ] 
    hour_glass_reset =[0, 1, 2, 1, 0, 1, 2]
    sum =0
    stop= [5,5]
    max =0
    while hour_glass[len(hour_glass) -1] != stop:
        if hour_glass[len(hour_glass) - 1][1] >= 5:

            for couple in hour_glass:
                couple[0] += 1

            for i in range(len(hour_glass)):
                hour_glass[i][1] = hour_glass_reset[i]

        for pos in hour_glass:
            sum += d_array[pos[0]][pos[1]]
        if sum > max:
            max = sum
        sum = 0
        for couple in hour_glass:
            couple[1] += 1
        
    return max
        
if __name__ == "__main__":
    test_list = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    test_list_2=[
        [-9, -9, -9, 1, 1, 1], 
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    print(hourglass_max_sum(test_list_2))