"""
2D Array - DS

THis function should take a random 6x6 array and postion wise get a sum of all of the elements in the
"""

def hourglass_max_sum(d_array: list) -> int:
    # print(d_array)
    hour_glass =[ [0,0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2,2] ] 
    horizonatal= 0
    vertical = 0
    sum =0
    while horizonatal <= 3:
        print(hour_glass)
        # if horizonatal ==
        for pos in hour_glass:
            # print(pos[0])
            sum += d_array[pos[0]][pos[1]]
        print(sum)
        for couple in hour_glass:
            couple[1] += 1
        
        horizonatal +=1
if __name__ == "__main__":
    test_list = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    hourglass_max_sum(test_list)