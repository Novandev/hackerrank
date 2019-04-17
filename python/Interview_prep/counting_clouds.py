"""
Counting Clouds:
This function will loop over a binary array and based on the elements being either
 a 1 ( for a thundercloud) or a 0 ( for a safe cloud), will plan the shortest path to win a game

"""

def counting_clouds(cloud_array: list) -> int:
    """
    Params: cloud_array - An array of binary numbers
    Return: best_step_count - An integer of the best recorded steps a path might have
    """
    total_step_count = [len([cloud for cloud in cloud_array if cloud == 0])]
    skip = False
    for i in range(len(cloud_array)-2):
        if cloud_array[i] == 0 and cloud_array[i] == cloud_array[i +1]:
            skip = True




