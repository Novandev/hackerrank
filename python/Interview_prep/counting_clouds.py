"""
Counting Clouds:
This function will loop over a binary array and based on the elements being either
 a 1 ( for a thundercloud) or a 0 ( for a safe cloud), will plan the shortest path to win a game
[0,0,1,0,0,1,0]
"""

def counting_clouds(cloud_array: list) -> int:
    """
    Params: cloud_array - An array of binary numbers
    Return: best_step_count - An integer of the best recorded steps a path might have
    """
    total_step_count = 0 # Total step count
    counter = 0 # sentinel to keep a counter going to track positions ahead of it
    arr_len = len(cloud_array) -1 # need a value to make sure we dont run over index in list
    while counter < arr_len: # while the counter value is less than the array length
        if counter + 2 >= arr_len or cloud_array[counter + 2] == 1: # Check two position ahead and check if the next
                                                                    # two spaces is a one
            counter += 1 # increase the counter
            total_step_count += 1 # increase total count
        else:
            counter += 2
            total_step_count += 1
    return total_step_count


if __name__ == "__main__":
    print(counting_clouds([0,1,0,0,0,1,0]))