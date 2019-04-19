"""
2D Array - DS

THis function should take a random 6x6 array and postion wise get a sum of all of the elements in the
"""

def hourglass_max_sum(d_array: list) -> int:
    # print(d_array)
    hour_glass =[ [0,0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2,2] ] 
    hour_glass_reset =[0, 1, 2, 1, 0, 1, 2]
    horizontal= 0
    vertical = 0
    sum =0
    stop= [5,5]
    while hour_glass[len(hour_glass) -1] != stop:
        # print(hour_glass)

        if hour_glass[len(hour_glass) - 1][1] == 5:
            for i in range(len(hour_glass) -1):
                print(hour_glass[i])
                hour_glass[i][1] = hour_glass_reset[i]
            print(hour_glass)
            for couple in hour_glass:
                couple[0] += 1
            print(hour_glass)

        for pos in hour_glass:
            # print(pos[1])
            sum += d_array[pos[0]][pos[1]]
        for couple in hour_glass:
            couple[1] += 1
        horizontal +=1 
        
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