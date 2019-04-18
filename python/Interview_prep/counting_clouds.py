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
    total_step_count = 0
    skip_count = 0
    for cloud in range(len(cloud_array) - 2):
    
        if cloud_array[cloud] == 1 or skip_count > 0:
            skip_count -= 1
            continue
        if cloud_array[cloud] == 0:
            total_step_count += 1
        elif cloud_array[cloud] == 0 and cloud_array[cloud + 1] == 0:
            total_step_count += 1
            skip_count += 1
    return total_step_count

if __name__ == "__main__":
    print(counting_clouds([0,1,0,0,0,1,0]))
    print(counting_clouds([0, 0, 0, 1, 0, 0]))